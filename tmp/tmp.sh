
word='td=100-50'
[ "`echo $word | grep 'td=[0-9]+-[0-9]+'`" ] && echo 'hey1'
[ "`echo $word | grep 'td=100-50'`" ] && echo 'hey2'
[ "`echo $word | grep 'td=100-[0-9][0-9]'`" ] && echo 'hey3'
[ "`echo $word | grep 'td=100-[0-9]\+'`" ] && echo 'hey4'
