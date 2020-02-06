echo "Thanks for using my script - checkout christianfjung.com for more. 
Takes 1 Argument: Name  of ipynb. To stop, CTRL-C in Terminal or Stop Button in JN. 

"
jupyter nbconvert   --to script $1.ipynb
awk '!/ipython/' $1.py >  temp.py && mv temp.py app.py && rm $1.py
streamlit run app.py
