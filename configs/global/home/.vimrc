source $VIMRUNTIME/defaults.vim

colorscheme slate
highlight Normal ctermfg=white ctermbg=black
set mouse-=a
set number
set foldcolumn=1

set expandtab
set smarttab
set smartindent
set tabstop=2
set softtabstop=2
set shiftwidth=2
set nowrap

function SudoWrite()
    w !sudo tee % > /dev/null
    e!
endfunction

command W call SudoWrite()
command Wq call SudoWrite() | quit

