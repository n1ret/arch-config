function mkcode() {
  mkdir -p $1 && code $1
}

function mkcodee() {
  mkcode $1 && exit
}

function codee() {
  code $1 && exit
}

alias ssh="kitten ssh"

alias n="nvim"
alias se="sudoedit"

