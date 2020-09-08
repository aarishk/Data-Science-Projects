# **ANALYSIS AND COMPUTATION ON MOVIES**
Creates a recommender system for movies using data from IMDB and GroupLens. All 
programs are either python programs or jupyter notebooks.

# Required Libraries:
* scikit-learn
* statsmodels
* matplotlib
* pandas
* numpy
* scipy

# Part 1: Recommender System 

**item based recommender.ipynb :**

Input Arguements: None

Output:
  * Various tables at different cell locations
  * The list of recommendations at the last cell.

To run the .ipynb, the cells must be executed from top to bottom sequentially
or by clicking 'Run all' under the cells tab in jupyter.

If a user wants to select a different target movie, simply change the 'mv'
variable in the last cell to the desired movie.

# Part 2: What factors influence the average rating of a movie?

**Order of execution:**
* 2_initial_data_cleaning.py
* 2_clean_data_for_ratings_analysis.py
* Any Jupyter File starting with "2."

**2_initial_data_cleaning.py :**

Command to run program:
`python3 2_initial_data_cleaning.py`

Files Required for program to run:
* "Data/title.basics.tsv.gz" (not included in repository due to size - Can be obtained from IMDB)
* "Data/title.ratings.tsv.gz" (not included in repository due to size - Can be obtained from IMDB)

Output: 
* "Data/title_basics_cleaned.gz"
* "Data/title_ratings_cleaned.gz"


**2_clean_data_for_ratings_analysis.py :**

Command to run program:
`python3 2_clean_data_for_ratings_analysis.py`

Files Required for program to run:
* "Data/title_basics_cleaned.gz"
* "Data/title_ratings_cleaned.gz"

Output: 
* "Data/title_basics_for_ratings_analysis.gz"


**Any Jupyter file starting with "2."**

Files include:
* 2.3.1 Rating and Year.ipynb
* 2.3.2 Ratings and Adult Movies.ipynb
* 2.3.3 Ratings and Length of a movie.ipynb
* 2.3.4 Rating and Genre.ipynb
* 2.4 Predicting Ratings.ipynb

How to run program:
All files need to be run in Jupyter. All output can be seen within each notebook.

Files Required for program to run:
* "Data/title_basics_cleaned.gz"
* "Data/title_ratings_cleaned.gz"

Output: NONE



# Part 3: Movielens dataset analysis

**movielens-analysis.py :**

Input Arguements: NONE

Output:
  * plot images to directory plot
  * Prints ANOVA p-Value of genre vs ratings
  * Prints top 3 recommended movies for each popular genre.


To run the movielens analysis function simply use the following command:

`python3 movielens-analysis.py`

If the output images are not being saved to plot the user must first create the
directory plot.


**movielens-ml.py :**

Input Arguements: NONE

Output:
  * 1 plot image of rating frequency to directory plot
  * Prints accuracy of selected machine learning models.
  * Prints top 10 recommended movies using knn.


To run the movielens machine learning program simply use the following command:

`python3 movielens-ml.py`

If user wants to select a different movie to recommend change the variable
on line 32 "movie_title" to the desired movie.

If the output images are not being saved to plot the user must first create the
directory plot.




