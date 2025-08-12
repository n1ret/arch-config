# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

if command -v nvim > /dev/null; then
  export SUDO_EDITOR=nvim
fi

if [ "$TERM_PROGRAM" = "vscode" ]; then
    alias gwd='cd "$VCS_STATUS_WORKDIR"'
fi

# Use powerline
USE_POWERLINE="true"
# Has weird character width
# Example:
#    is not a diamond
HAS_WIDECHARS="false"
# Use zsh configuration
if [[ -e /usr/share/zsh/zsh-config ]]; then
  source /usr/share/zsh/zsh-config
fi
# Use zsh prompt
if [[ -e /usr/share/zsh/zsh-prompt ]]; then
  source /usr/share/zsh/zsh-prompt
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

[[ ! -f ~/.aliases.zsh ]] || source ~/.aliases.zsh
[[ ! -f ~/.startup.zsh ]] || source ~/.startup.zsh
