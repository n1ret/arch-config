source $VIMRUNTIME/defaults.vim

colorscheme slate
highlight Normal ctermfg=white ctermbg=black
set mouse-=a
set number
set foldcolumn=1

set expandtab
set smarttab
set smartindent
set tabstop=4
set softtabstop=4
set shiftwidth=4

command W w !sudo tee > /dev/null %

