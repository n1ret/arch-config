function mkcode() {
  for arg in "$@"; do
    mkdir -p "$arg" || return 1
  done

  code "$@"
  return $?
}

function mkcodee() {
  mkcode "$@" && exit
}

function codee() {
  code "$@" && exit
}

if [ "$TERM_PROGRAM" = "vscode" ]; then
  alias gwd='cd "$VSCODE_CWD"'
fi

if [ "$TERM" = "xterm-kitty" ]; then
  alias ssh="kitten ssh"
fi

alias n="nvim"

alias se="sudoedit"
alias visudo="sudo SUDO_EDITOR=vim visudo"

