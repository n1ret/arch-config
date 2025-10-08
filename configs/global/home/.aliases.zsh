function mkcode() {
  mkdir -p $1 && code $1
}

function mkcodee() {
  mkcode $1 && exit
}

function codee() {
  code $1 && exit
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

