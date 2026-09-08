"""Small deterministic Ω-Math v0.9 text parser.

Syntax is intentionally explicit and typed:
  entity A 0
  entity B 1
  relation A B +1
  path P = A->B->C
  sign P
  dist A B

This is a reference syntax, not a claim that one surface syntax is canonical.
"""
import re
from .core import Entity, Relation, Path, Configuration

class ParseError(ValueError): pass

class Program:
    def __init__(self): self.entities={}; self.relations={}; self.paths={}; self.results=[]

    def run(self, text):
        p=self
        for no, raw in enumerate(text.splitlines(),1):
            line=raw.strip()
            if not line or line.startswith('#'): continue
            try: self._line(line)
            except Exception as e: raise ParseError(f"line {no}: {e}") from e
        return self.results

    def _line(self,line):
        m=re.fullmatch(r"entity\s+(\S+)\s+([01])",line)
        if m: self.entities[m.group(1)]=Entity(m.group(1),int(m.group(2))); return
        m=re.fullmatch(r"relation\s+(\S+)\s+(\S+)\s+([+-]1)(?:\s+(\S+))?",line)
        if m:
            a,b,s,k=m.groups(); self.relations[k or f"{a}->{b}#{len(self.relations)}"]=Relation(a,b,int(s)); return
        m=re.fullmatch(r"path\s+(\S+)\s*=\s*(\S+(?:->\S+)*)",line)
        if m:
            name, nodes=m.groups(); ids=nodes.split('->'); rs=[]
            for a,b in zip(ids,ids[1:]):
                candidates=[r for r in self.relations.values() if r.src==a and r.dst==b]
                if not candidates: raise ValueError(f"missing relation {a}->{b}")
                rs.append(candidates[0])
            self.paths[name]=Path(tuple(rs),ids[0],ids[-1]); return
        m=re.fullmatch(r"(dist|sign|cycle|path_eq)\s+(.+)",line)
        if m:
            op,rest=m.groups(); args=rest.split()
            if op=='dist':
                if len(args)!=2: raise ValueError('DIST needs two entities')
                self.results.append(0 if self.entities[args[0]]==self.entities[args[1]] else 1)
            elif op=='sign': self.results.append(self._sign(self.paths[args[0]]))
            elif op=='cycle': self.results.append(self.paths[args[0]].length>0 and self.paths[args[0]].source==self.paths[args[0]].target)
            else: self.results.append(self.paths[args[0]]==self.paths[args[1]])
            return
        raise ValueError('unsupported syntax')

    @staticmethod
    def _sign(p):
        out=1
        if not p.relations: raise ValueError('SIGN requires non-empty path')
        for r in p.relations: out*=r.sign
        return out
