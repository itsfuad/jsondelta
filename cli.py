import argparse
import json
from jsondelta import compare


def main(argv=None):
    parser = argparse.ArgumentParser(description='Diff JSON by key path')
    parser.add_argument('before')
    parser.add_argument('after')
    parser.add_argument('--json', action='store_true', help='Machine-readable changes')
    args = parser.parse_args(argv)
    with open(args.before, encoding='utf8') as stream: left = json.load(stream)
    with open(args.after, encoding='utf8') as stream: right = json.load(stream)
    changes = compare(left,right)
    if args.json: print(json.dumps([{'path': p, 'kind': k, 'before': a, 'after': b} for p,k,a,b in changes],indent=2))
    else:
        for path,kind,old,new in changes:
            print('%-8s %s: %r -> %r' % (kind,path,old,new))
        print('%d difference(s)' % len(changes))
    return 1 if changes else 0


if __name__ == '__main__': raise SystemExit(main())
