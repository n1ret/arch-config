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

