import argparse
import os

version = {}

parser = argparse.ArgumentParser(
    prog='Versioning',
    description='Updates the version',
    epilog='SimpleRose Inc')

parser.add_argument( '--major',
                     action='store_true')  # on/off flag
parser.add_argument( '--minor',
                    action='store_true')  # on/off flag
parser.add_argument('--patch',
                    action='store_true')  # on/off flag
parser.add_argument('filename')

args = parser.parse_args()
# print(args.patch)
# print(args.filename)
# print(os.path.abspath(args.filename))

# load version file
with open(os.path.abspath(args.filename), 'r') as version_file:
    contents = version_file.read()
    split_contents = contents.split('.')

    # print(version)
    version['major'] = int(split_contents[0])
    version['minor'] = int(split_contents[1])
    version['patch'] = int(split_contents[2])
    # print(version)
    # print(json.dumps(version, indent=3))

# if not((args.major and not args.minor and not args.patch) or \
#     (not args.major and args.minor and not args.patch) or \
#     (not args.major and not args.minor and args.patch)):
#     print('Exactly one of patch, minor or major must be a flag', file=sys.stderr)
#     exit(1)

if args.major:
    version['patch'] = 0
    version['minor'] = 0
    version['major'] += 1
if args.minor:
    version['patch'] = 0
    version['minor'] += 1
if args.patch:
    version['patch'] += 1

new_version = f'{version["major"]}.{version["minor"]}.{version["patch"]}'
print(new_version)

