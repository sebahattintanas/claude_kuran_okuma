run(){ t=$1; shift; r=$1; case $t in
 say) out=$(python3 oturum_say.py "$@" 2>/dev/null);;
 lem) out=$(python3 oturum_lem.py "$@" 2>/dev/null); r=$(echo $r|cut -d: -f1,2);;
 dizi) out=$(python3 oturum_lemdizi.py "$@" 2>/dev/null); r="$1:$2";;
 esac
 echo "### $t $*"; echo "$out" | head -c 1500; echo; echo "$out" | python3 /home/claude/sunum/sinifla.py $r; echo; }
