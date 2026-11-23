cd grandchild && cp results.txt /dev/null; rm -rf ../gc_rerun && mkdir ../gc_rerun && cp control.py run.py ../gc_rerun/ && cd ../gc_rerun && python3 control.py && python3 run.py
