
# UNIX level aliases
alias cd..="cd .."
alias ..="cd ../.."
alias ...="cd ../../.."
alias clr="clear" # Clear your terminal screen
alias ip="curl icanhazip.com" # Your public IP address
alias ll="ls -al" # List all files in current directory in long list format
alias ldir="ls -al | grep ^d" # List all directories in current directory in long list format
alias o="open ." # Open the current directory in Finder
alias ut="uptime" # Computer uptime
alias cat='bat'
alias search='grep -rnw . -e'
alias preview="fzf --preview 'bat --color \"always\" {}'"
# add support for ctrl+o to open selected file in VS Code
export FZF_DEFAULT_OPTS="--bind='ctrl-o:execute(code {})+abort'"

# Kubectl Aliases
alias ka="k8s-auth"
alias k="kubectl"
alias kns="kubens"
alias knsp="kubens performance"
alias ks="kubectx stg"
alias kd="kubectx dev"
alias kp="kubectx prod"
alias kcp="kubectl cp"
alias kgpo="kubectl get pods -o wide"
alias kgsvc="kubectl get svc -o wide"
alias kgnd="kubectl get node -o wide"
alias kpf="kubectl port-forward"
alias kdec="kubectl describe po"
alias hre="helm repo update"
alias kdel="kubectl -n performance delete deploy -l app=qa-api-performance"

function kloc(){
pod=$(kubectl get pods --namespace performance -l "app=qa-api-performance,release=qa-api-performance" -o jsonpath="{.items[0].metadata.name}") && kubectl exec -it -n performance $pod /bin/sh 
}

function kgcm() { kubectl get configmap $@ -o yaml; }

function kpod(){
pod=$(kubectl -n performance get po | grep "$@" | awk '{print $1}') && kubectl exec -it -n performance $pod bash
}

function sam(){
saml2aws login -a "$@" && export AWS_PROFILE="$@"
}

function kpfg(){
kubectl -n performance port-forward svc/qa-api-performance-grafana "$@":80
}

function kex() { 
result=$(kubectl get po | grep "$@" | awk '{print $1}')
exitCode=$?
if [ ! "$exitCode" -eq 0 ]; then
    echo "Could not find pod matching [$@]."
    return 1;       
fi
kubectl exec -ti $result bash 
}

function kpfg(){
kubectl -n performance port-forward svc/qa-api-performance-grafana "$@":80
}

function kexsh() {
result=$(kubectl get po | grep "$@" | awk '{print $1}')
exitCode=$?
if [ ! "$exitCode" -eq 0 ]; then
    echo "Could not find pod matching [$@]."
    return 1;
fi
kubectl exec -ti $result sh
}

function kcph() { kubectl exec -ti $@ -- sh -c 'apk -q update; apk add -q curl jq; curl localhost:8080/__health | jq'; }

function gcm() { kubectl get configmap $@ -o yaml; }

function kclfl() { 
result=$(kubectl get po | grep "$1" | awk '{print $1}')
kubectl logs $result --tail=$2  -f; }

function kcready() {
for node in  $(kubectl get nodes | tail -n +2 | awk '{print $1}'); do
        echo $node
        echo -e "$(kubectl describe node $node | grep  "Ready")\n";
done
}

# Git Aliases
alias gs='git status'
alias gss='git status -s'
alias gaa='git add -A'
alias gpu='git pull'
alias gph='git push'
alias gcc='git commit -a -m'
alias ghist='git log --oneline --graph --decorate --all'

function g_merge {
gpu origin master
gph origin "$@"
gck master
gpu origin "$@" 
}

alias gb='git branch'
alias gbr='git branch -r'
alias gbn='git checkout -b'
alias gck='git checkout'

#remove local branch
function gbdel {
	git branch -D "$1"
}

#delete remote branch
function gbrdel {
	git push origin :"$1"
}

#get a list of conflicts
alias conflicts='git diff --name-only --diff-filter=U'

function tf-release() {
    : "${1?Expected tag}"
    local tag="$1"
    GREN_GITHUB_TOKEN=$(<~/.github_token)
    export GREN_GITHUB_TOKEN
    ~/Documents/OfficialDocuments/Projects/docker-terraform/scripts/tf-release "$tag" "$tag"
    unset GREN_GITHUB_TOKEN
}

# Display the list of shortcuts
function all {
	echo "
- - - - - - - - - - - - - -
UNIX Convenience Shortcuts:
- - - - - - - - - - - - - -

alias clr=\"clear\" 
alias ip=\"curl icanhazip.com\"
alias ll=\"ls -al\"
alias ldir=\"ls -al | grep ^d\" 
alias o=\"open .\" 
alias ut=\"uptime\" 
alias cat=\"bat\"
alias preview=\"fzf --preview 'bat --color \"always\" {}'\"
alias search=grep -rnw . -e

- - - - - - - - - - - - - -
Kubectl Convenience Shortcuts:
- - - - - - - - - - - - - -
alias ka=k8s-auth
alias k=\"kubectl\"
alias kns=\"kubens\"
alias knsp=\"kubens performance\"
alias ks=\"kubectx stg\"
alias kd=\"kubectx dev\"
alias kp=\"kubectx prod\"
alias kcp=\"kubectl cp\"
alias kgnd=\"kubectl get node -o wide\"
alias kgpo=\"kubectl get pods -o wide\"
alias kgsvc=\"kubectl get svc -o wide\"
alias kpf=\"kubectl port-forward\"
alias hre=\"helm repo update\"

function kgcm() - Get config map
function kloc() - Login to locust pod for dev/stg
function sam() - Authentical against saml2aws and export aws
function kex() - Connect to a pod as bash
function kexsh() = Connect to a pod as sh
function kpfg() - Port forward grafana to desired port
function gcm() - Get config map for chart
function kclfl() - Get logs for the pod Syntax: kclfl pod name linenum
function kcready() - Provide the list of ready pods

- - - - - - - - - - - - - -
GIT Convenience Shortcuts:
- - - - - - - - - - - - - -
alias gs='git status'
alias gss='git status -s'
alias gaa='git add -A'
alias gpu='git pull'
alias gph='git push'
alias gb='git branch'
alias gbr='git branch -r'
alias gbn='git checkout -b'
alias gck='git checkout'
alias conflicts='git diff --name-only --diff-filter=U' #get a list of conflicts

function gc -- commit and show git status #gc "Message"
function tf-release -- creates a release for git repo
-- remove local branch
function gbdel 

-- delete remote branch
function gbrdel 

- - - - - - - - - - - - - -
"
}
