DATA_DIR := data
DATA_PREFIX := dataset_

clasico:
	glpsol -m tp-clasico.mod -d $(DATA_DIR)/$(DATA_PREFIX)$(SET).dat -o sol-$(SET).sol


cplex:
	glpsol --check --model tp-clasico.mod --wlp tp-clasico-$(SET).lp --log convert.log --data $(DATA_DIR)/$(DATA_PREFIX)$(SET).dat
	cplex -c "read tp-clasico-$(SET).lp" "mipopt" "write sol-$(SET)-clpex.xml" "sol" "y"

clean:
	rm -f *.csv
	rm -f *.log
	rm -f *.sol
	rm -f *.xml
	rm -f *.gv
	rm -f *.lp
