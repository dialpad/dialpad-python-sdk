#!/bin/bash

DOC="Build and release a new version of the python-dialpad package.

Usage:
  create_version.sh [-h] [--patch|--minor|--major] [--bump-only|--no-upload]

By default, this script will:
1  -  Run the tests
2  -  Check that we're on master
3  -  Bump the patch-number in setup.py
4  -  Check whether there are any remote changes that haven't been pulled
5  -  Build the distribution package
6  -  Verify the package integrity
7  -  Commit the patch-number bump
8  -  Tag the release
9  -  Upload the package to PyPI
10 -  Push the commit and tag to github

If anything fails along the way, the script will bail out.

Options:
  -h --help    Show this message
  --patch      Bump the patch version number (default)
  --minor      Bump the minor version number
  --major      Bump the major version number
  --bump-only  Make the appropriate version bump, but don't do anything else
               (i.e. stop after performing step 3)
  --no-upload  Do everything other than uploading the package to PyPI
               (i.e. skip step 9)
"
# docopt parser below, refresh this parser with `docopt.sh create_release.sh`
# shellcheck disable=2016,1075
docopt() { parse() { if ${DOCOPT_DOC_CHECK:-true}; then local doc_hash
doc_hash=$(printf "%s" "$DOC" | shasum -a 256)
if [[ ${doc_hash:0:5} != "$digest" ]]; then
stderr "The current usage doc (${doc_hash:0:5}) does not match \
what the parser was generated with (${digest})
Run \`docopt.sh\` to refresh the parser."; _return 70; fi; fi; local root_idx=$1
shift; argv=("$@"); parsed_params=(); parsed_values=(); left=(); testdepth=0
local arg; while [[ ${#argv[@]} -gt 0 ]]; do if [[ ${argv[0]} = "--" ]]; then
for arg in "${argv[@]}"; do parsed_params+=('a'); parsed_values+=("$arg"); done
break; elif [[ ${argv[0]} = --* ]]; then parse_long
elif [[ ${argv[0]} = -* && ${argv[0]} != "-" ]]; then parse_shorts
elif ${DOCOPT_OPTIONS_FIRST:-false}; then for arg in "${argv[@]}"; do
parsed_params+=('a'); parsed_values+=("$arg"); done; break; else
parsed_params+=('a'); parsed_values+=("${argv[0]}"); argv=("${argv[@]:1}"); fi
done; local idx; if ${DOCOPT_ADD_HELP:-true}; then
for idx in "${parsed_params[@]}"; do [[ $idx = 'a' ]] && continue
if [[ ${shorts[$idx]} = "-h" || ${longs[$idx]} = "--help" ]]; then
stdout "$trimmed_doc"; _return 0; fi; done; fi
if [[ ${DOCOPT_PROGRAM_VERSION:-false} != 'false' ]]; then
for idx in "${parsed_params[@]}"; do [[ $idx = 'a' ]] && continue
if [[ ${longs[$idx]} = "--version" ]]; then stdout "$DOCOPT_PROGRAM_VERSION"
_return 0; fi; done; fi; local i=0; while [[ $i -lt ${#parsed_params[@]} ]]; do
left+=("$i"); ((i++)) || true; done
if ! required "$root_idx" || [ ${#left[@]} -gt 0 ]; then error; fi; return 0; }
parse_shorts() { local token=${argv[0]}; local value; argv=("${argv[@]:1}")
[[ $token = -* && $token != --* ]] || _return 88; local remaining=${token#-}
while [[ -n $remaining ]]; do local short="-${remaining:0:1}"
remaining="${remaining:1}"; local i=0; local similar=(); local match=false
for o in "${shorts[@]}"; do if [[ $o = "$short" ]]; then similar+=("$short")
[[ $match = false ]] && match=$i; fi; ((i++)) || true; done
if [[ ${#similar[@]} -gt 1 ]]; then
error "${short} is specified ambiguously ${#similar[@]} times"
elif [[ ${#similar[@]} -lt 1 ]]; then match=${#shorts[@]}; value=true
shorts+=("$short"); longs+=(''); argcounts+=(0); else value=false
if [[ ${argcounts[$match]} -ne 0 ]]; then if [[ $remaining = '' ]]; then
if [[ ${#argv[@]} -eq 0 || ${argv[0]} = '--' ]]; then
error "${short} requires argument"; fi; value=${argv[0]}; argv=("${argv[@]:1}")
else value=$remaining; remaining=''; fi; fi; if [[ $value = false ]]; then
value=true; fi; fi; parsed_params+=("$match"); parsed_values+=("$value"); done
}; parse_long() { local token=${argv[0]}; local long=${token%%=*}
local value=${token#*=}; local argcount; argv=("${argv[@]:1}")
[[ $token = --* ]] || _return 88; if [[ $token = *=* ]]; then eq='='; else eq=''
value=false; fi; local i=0; local similar=(); local match=false
for o in "${longs[@]}"; do if [[ $o = "$long" ]]; then similar+=("$long")
[[ $match = false ]] && match=$i; fi; ((i++)) || true; done
if [[ $match = false ]]; then i=0; for o in "${longs[@]}"; do
if [[ $o = $long* ]]; then similar+=("$long"); [[ $match = false ]] && match=$i
fi; ((i++)) || true; done; fi; if [[ ${#similar[@]} -gt 1 ]]; then
error "${long} is not a unique prefix: ${similar[*]}?"
elif [[ ${#similar[@]} -lt 1 ]]; then
[[ $eq = '=' ]] && argcount=1 || argcount=0; match=${#shorts[@]}
[[ $argcount -eq 0 ]] && value=true; shorts+=(''); longs+=("$long")
argcounts+=("$argcount"); else if [[ ${argcounts[$match]} -eq 0 ]]; then
if [[ $value != false ]]; then
error "${longs[$match]} must not have an argument"; fi
elif [[ $value = false ]]; then
if [[ ${#argv[@]} -eq 0 || ${argv[0]} = '--' ]]; then
error "${long} requires argument"; fi; value=${argv[0]}; argv=("${argv[@]:1}")
fi; if [[ $value = false ]]; then value=true; fi; fi; parsed_params+=("$match")
parsed_values+=("$value"); }; required() { local initial_left=("${left[@]}")
local node_idx; ((testdepth++)) || true; for node_idx in "$@"; do
if ! "node_$node_idx"; then left=("${initial_left[@]}"); ((testdepth--)) || true
return 1; fi; done; if [[ $((--testdepth)) -eq 0 ]]; then
left=("${initial_left[@]}"); for node_idx in "$@"; do "node_$node_idx"; done; fi
return 0; }; either() { local initial_left=("${left[@]}"); local best_match_idx
local match_count; local node_idx; ((testdepth++)) || true
for node_idx in "$@"; do if "node_$node_idx"; then
if [[ -z $match_count || ${#left[@]} -lt $match_count ]]; then
best_match_idx=$node_idx; match_count=${#left[@]}; fi; fi
left=("${initial_left[@]}"); done; ((testdepth--)) || true
if [[ -n $best_match_idx ]]; then "node_$best_match_idx"; return 0; fi
left=("${initial_left[@]}"); return 1; }; optional() { local node_idx
for node_idx in "$@"; do "node_$node_idx"; done; return 0; }; switch() { local i
for i in "${!left[@]}"; do local l=${left[$i]}
if [[ ${parsed_params[$l]} = "$2" ]]; then
left=("${left[@]:0:$i}" "${left[@]:((i+1))}")
[[ $testdepth -gt 0 ]] && return 0; if [[ $3 = true ]]; then
eval "((var_$1++))" || true; else eval "var_$1=true"; fi; return 0; fi; done
return 1; }; stdout() { printf -- "cat <<'EOM'\n%s\nEOM\n" "$1"; }; stderr() {
printf -- "cat <<'EOM' >&2\n%s\nEOM\n" "$1"; }; error() {
[[ -n $1 ]] && stderr "$1"; stderr "$usage"; _return 1; }; _return() {
printf -- "exit %d\n" "$1"; exit "$1"; }; set -e; trimmed_doc=${DOC:0:1027}
usage=${DOC:64:83}; digest=b986d; shorts=(-h '' '' '' '' '')
longs=(--help --patch --minor --major --bump-only --no-upload)
argcounts=(0 0 0 0 0 0); node_0(){ switch __help 0; }; node_1(){
switch __patch 1; }; node_2(){ switch __minor 2; }; node_3(){ switch __major 3
}; node_4(){ switch __bump_only 4; }; node_5(){ switch __no_upload 5; }
node_6(){ optional 0; }; node_7(){ either 1 2 3; }; node_8(){ optional 7; }
node_9(){ either 4 5; }; node_10(){ optional 9; }; node_11(){ required 6 8 10; }
node_12(){ required 11; }; cat <<<' docopt_exit() {
[[ -n $1 ]] && printf "%s\n" "$1" >&2; printf "%s\n" "${DOC:64:83}" >&2; exit 1
}'; unset var___help var___patch var___minor var___major var___bump_only \
var___no_upload; parse 12 "$@"; local prefix=${DOCOPT_PREFIX:-''}
local docopt_decl=1; [[ $BASH_VERSION =~ ^4.3 ]] && docopt_decl=2
unset "${prefix}__help" "${prefix}__patch" "${prefix}__minor" \
"${prefix}__major" "${prefix}__bump_only" "${prefix}__no_upload"
eval "${prefix}"'__help=${var___help:-false}'
eval "${prefix}"'__patch=${var___patch:-false}'
eval "${prefix}"'__minor=${var___minor:-false}'
eval "${prefix}"'__major=${var___major:-false}'
eval "${prefix}"'__bump_only=${var___bump_only:-false}'
eval "${prefix}"'__no_upload=${var___no_upload:-false}'; local docopt_i=0
for ((docopt_i=0;docopt_i<docopt_decl;docopt_i++)); do
declare -p "${prefix}__help" "${prefix}__patch" "${prefix}__minor" \
"${prefix}__major" "${prefix}__bump_only" "${prefix}__no_upload"; done; }
# docopt parser above, complete command for generating this parser is `docopt.sh create_release.sh`

# Run that auto-generated mess above to parse the command-line args.
eval "$(docopt "$@")"

if [ $__major == "true" ]; then
  VERSION_PART="major"
elif [ $__minor == "true" ]; then
  VERSION_PART="minor"
else
  VERSION_PART="patch"
fi

# bump-only implies no-upload from a practical perspective.
if [ $__bump_only == "true" ]; then
  __no_upload="true"
fi

bail_out() {
  popd &> /dev/null
  exit 1
}

confirm() {
  if [ -z "$*" ]; then
    read -p "Shall we proceed? (y/N)" -r confirmation
  else
    read -p "$*" -r confirmation
  fi
  if [[ ! $confirmation =~ ^[Yy]$ ]]; then
    bail_out
  fi
  echo
}

REPO_DIR=`dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"`

pushd $REPO_DIR &> /dev/null

# Do a safety-confirmation if the user is about to do something that isn't trivial to undo.
if [ $__bump_only == "false" ]; then
  if [ $__no_upload == "true" ]; then
    echo "You're about to build and push a new ($VERSION_PART) release to Github"
    echo "(Although we won't upload the package to PyPI)"
  else
    echo "You're about to build and push a new ($VERSION_PART) release to Github AND PyPI"
  fi
  confirm "Are you sure that's what you want to do? (y/N)"
fi

# Do some sanity checks to make sure we're in a sufficient state to actually do what the user wants.

# If we're planning to do more than just bump the version, then make sure "twine" is installed.
if [[ $__bump_only == "false" ]]; then
  if ! command -v twine &> /dev/null; then
    echo "You must install twine (pip install twine) if you want to upload to PyPI"
    bail_out
  fi
fi

# Make sure we're on master (but let the user proceed if they reeeeally want to).
branch_name=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
if [ "$branch_name" != "master" ]; then
  echo "We probably shouldn't be bumping the version number if we're not on the master branch."
  confirm "Are you this is want you want? (y/N)"
fi

# Run the unit tests and make sure they're passing.
test_failure_prompt="Are you *entirely* sure you want to release a build with failing tests? (y/N)"
tox || confirm "There are failing tests. $test_failure_prompt"

# If we're *only* bumping the version, then we're safe to proceed at this point.
if [ $__bump_only == "true" ]; then
  tox -e bump $VERSION_PART
  exit
fi

# In any other scenario, we should make sure the working directory is clean, and that we're
# up-to-date with origin/master
if ! git pull origin master --dry-run -v 2>&1 | grep "origin/master" | grep "up to date" &> /dev/null; then
  echo "There are changes that you need to pull on master."
  bail_out
fi

# We'll let bump2version handle the dirty-working-directory scenario.
tox -e bump $VERSION_PART || bail_out

# Now we need to build the package, so let's clear away any junk that might be lying around.
rm -rf ./dist &> /dev/null
rm -rf ./build &> /dev/null

# The build stdout is a bit noisy, but stderr will be helpful if there's an error.
tox -e build > /dev/null || bail_out

# Make sure there aren't any issues with the package.
twine check dist/* || bail_out

# Upload the package if that's desirable.
if [ $__no_upload == "false" ]; then
  twine upload dist/* || bail_out
fi

# Finally, commit the changes, tag the commit, and push.
git add .
new_version=`cat .bumpversion.cfg | grep "current_version = " | sed  "s/current_version = //g"`
git commit -m "Release version $new_version"
git tag -a "v$new_version" -m "Release version $new_version"

git push origin master
git push origin "v$new_version"

echo "Congrats!"
if [ $__no_upload == "true" ]; then
  echo "The $new_version release commit has been pushed to GitHub, and tagged as \"v$new_version\""
else
  echo "The $new_version release is now live on PyPI, and tagged as \"v$new_version\" on GitHub"
fi

popd &> /dev/null
