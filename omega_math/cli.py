import argparse, json, sys
from .parser import Program, ParseError

def main(argv=None):
    ap=argparse.ArgumentParser(prog='omega-math', description='Ω-Math v0.9 reference interpreter')
    ap.add_argument('file', nargs='?', help='Ω-Math source file; stdin if omitted')
    ns=ap.parse_args(argv)
    text=open(ns.file,encoding='utf-8').read() if ns.file else sys.stdin.read()
    try: out=Program().run(text)
    except ParseError as e: ap.error(str(e))
    for x in out: print(json.dumps(x, ensure_ascii=False, default=str))
    return 0

if __name__ == '__main__': raise SystemExit(main())
