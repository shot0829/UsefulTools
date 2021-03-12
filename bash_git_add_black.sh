git_bin=`which git`
function git () {
    if [[ $1 == 'add' ]];then
        args_list=${@:2}
        for i in $args_list;
        do
            if [[ $i == *.py ]];then
                echo "black $i"
                black $i
            fi
        done
    fi  
    bash -c "$git_bin $(printf ' %q' "$@")"
}
