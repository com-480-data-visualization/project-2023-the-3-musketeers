# Project of Data Visualization (COM-480)

| Student's name | SCIPER |
|----------------|--------|
| Zhan Li        | 351592 |
| Dong Chu       | 352494 |
| Dana Kalaaji   | 289583 |

[Milestone 1](#milestone-1) • [Milestone 2](#milestone-2) • [Milestone 3](#milestone-3)

## Milestone 1 (23rd April, 5pm)

**10% of the final grade**

This is a preliminary milestone to let you set up goals for your final project and assess the feasibility of your ideas.
Please, fill the following sections about your project.

*(max. 2000 characters per section)*

### Dataset 🍫 

<!-- > Find a dataset (or multiple) that you will explore. Assess the quality of the data it contains and how much preprocessing / data-cleaning it will require before tackling visualization. We recommend using a standard dataset as this course is not about scraping nor data processing.
>
> Hint: some good pointers for finding quality publicly available datasets ([Google dataset search](https://datasetsearch.research.google.com/), [Kaggle](https://www.kaggle.com/datasets), [OpenSwissData](https://opendata.swiss/en/), [SNAP](https://snap.stanford.edu/data/) and [FiveThirtyEight](https://data.fivethirtyeight.com/)), you could use also the DataSets proposed by the ENAC (see the Announcements section on Zulip). -->

As Switzerland is renowned for its chocolate, we embarked on a project to investigate the factors that influence the quality of chocolate. To achieve this goal, we utilized the [Chocolate Bar Ratings](http://flavorsofcacao.com/database_w_REF.html), which comprises the ratings given by experts to over 2600 chocolate bars using the Flavors of Cacao Rating System. This system rates each chocolate on a scale from Unpleasant (rating=1) to Elite (rating=5). The dataset also contains additional background information, such as the chocolate maker, specific bean origin, broad bean origin, REF value, review date, cocoa percentage, company location, date of review, company region, ingredients and most memorable characteristics. This dataset can be stored in a csv file consisting of 2632 rows and 10 columns:
* REF: A numeric value that uniquely identifies each chocolate bar in the database.
* Company (Manufacturer): The name of the company that produced the chocolate bar.
* Company Location: The location of the company that produced the chocolate bar.
* Review Date: The year in which the chocolate bar was rated.
* Country of Bean Origin: The country where the cocoa beans used in the chocolate bar were grown.
* Specific Bean Origin or Bar Name: The specific region, farm, or name of the cocoa beans used in the chocolate bar, if available.
* Cocoa Percent: The percentage of cocoa solids in the chocolate bar.
* Ingredients: A description of the ingredients used in the chocolate bar.
* Most Memorable Characteristics: A free-form text field where reviewers can describe the most memorable characteristics of the chocolate bar.
* Rating: A numeric rating on a scale from 1 (Unpleasant) to 5 (Elite), indicating the overall quality of the chocolate bar.

The dataset comprises three different data types: *int* (for REF value and review data), *float* (for ratings) and *str* (for all other attributes). However, we observed that 87 out of 2632 data points for ingredients were null. Several approaches could be employed to address missing values for this variable, including inferring them from the specific bean origin. Overall, the dataset is relatively clean.

We are aware of the fact that there are always some limitations to consider even if the Chocolate Bar Ratings dataset gives us a lot of information on over 2600 chocolate bars. In our case, our limitations would be the fact that it's missing some important information such as the price or the packaging, which could also impact the chocolate quality. But even with these limitations, the dataset is still useful and has a lot of data that can be used for exploring the factors that impact chocolate quality and learning more about the chocolate industry.

### Problematic

<!-- > Frame the general topic of your visualization and the main axis that you want to develop.
> - What am I trying to show with my visualization?
> - Think of an overview for the project, your motivation, and the target audience. -->

Our motivations for this projects are to extract meaningful insights from the Chocolate Bar Ratings dataset, with the aim of helping chocolate makers formulate effective product-making strategies. Our target audience includes not only the chocolates manufacturers and retailers who want to improve their products quality and increase their sales, but also customers who want to understand the factors that contribute to a higher-quality chocolate to make informed decisions when buying it. Specifically, we seek to answer the following questions:

* To what extent does the cocoa percentage impact the chocolate rating?
* Does the type or origin of the bean influence the flavor of the chocolate? If yes which specific beans produce higher-rated chocolate and why?
* Is there a discernible trend in chocolate taste between 2006 and 2022?
* Have certain chocolate makers already adopted similar manufacturing practices?

To accomplish these objectives, we will process, analyze, and aggregate the data using appropriate techniques and visualization methods, such as geovisualization and time series analysis. By doing so, we aim to provide clear and insightful visualizations that can help our target audience make informed decisions about their products. 

### Exploratory Data Analysis

Our dataset consists of 2632 tuples. We wanted to get an initial understanding and checked the first 5 rows of the data frame to get a first glimpse.

![5_first_rows](https://user-images.githubusercontent.com/72870726/230516057-d837c8df-b048-44e7-8613-8f05e543ea9b.png)


Then we visualize some important variables to have some statistical insight on the data.

![country_bean_distribution](https://user-images.githubusercontent.com/72870726/230518147-612f9221-f229-48ea-84cd-1a95581754ed.png)

![company_location](https://user-images.githubusercontent.com/72870726/230518159-a09d8110-ee4c-44c8-8493-10961640f324.png)

![top15_companies](https://user-images.githubusercontent.com/72870726/230518376-c2afc5b2-62a0-4afd-987a-844949796630.png)



From the visualization, we found that:
- The majority of the companies are from the United States;
- However, the beans origins are mainly Central and South America;
- Soma is the company that sells the most chocolate bars, the other 14 biggest competitors sell approximately the same amount.



![Rating_distribution](https://user-images.githubusercontent.com/72870726/230518185-df33d328-69f9-4ac6-a677-1ee1fc144bc1.png)

![cocoa_distribution](https://user-images.githubusercontent.com/72870726/230518188-f21996da-0077-4f9d-a9f7-c523258a4d56.png)

![Cocoa Percent vs  Rating](https://user-images.githubusercontent.com/72870726/230518193-e65672dc-707f-485e-a9f5-1fe01660cd40.jpg)

Next, we examined the relationship between cocoa percent and rating:
- Most of the chocolate bars reviewed contains 70% of cocoa;
- There's a slight negative correlation between Cocoa Percent and Rating.
- The average rating of all chocolate bars in the dataset is 3.2/5 and doesn't exceed 4

Additionally, here are some information regarding the ingredients and the top 15 charcateristics found in these chocolate bars: 

![Most Used Ingredients in Chocolate](https://user-images.githubusercontent.com/72870726/230518216-e3879ec5-aa2e-4ff4-89a9-4ff3b860f575.png)

![Top 15 Most Present Characteristics](https://user-images.githubusercontent.com/72870726/230519592-0164f322-50fe-40c0-aafe-e0957590440d.png)

We see from here that there is a wide range of flavors available for chocolate. It would be interesting to further investigate the relationship between the flavor profile and type of bean used and the ingredients present in the chocolate bar.

We think that understanding these insights is important for chocolate manufacturers, distributors, and retailers who want to improve the quality of their products and make informed decisions about cocoa bean sourcing and type. Customers who want to buy high-quality chocolate can also benefit from these information.

### Related work

Some other work has some extensive exploratory data analysis to research [what characterize good chocolate](https://www.kaggle.com/code/allunia/how-good-does-your-chocolate-taste) and [the relationship between chocolate quality and the distribution of company locations](https://www.kaggle.com/code/fangya/chocolate-bar-rating-eda-anova-svm). However, they have mostly failed to provide insight into the correlated contribution of attributes to chocolate ratings.

We think our subject is worth tackling because nowadays there is an increased demand for high quality products made sustainably, and chocolate is directly concerned by this trend. Our ultimate goal is to provide clear and actionable insights to chocolate makers because by having a better understanding of the factors that influence chocolate quality, they can improve their products, stay competitive and propose better products for customers.

We took inspiration from following visualisations:
* [PBDB Navigator](https://paleobiodb.org/navigator/): Provides a great interface for browsing through space and time in paleobiology.
* [DivineComedy.Digital](https://divinecomedy.digital/#/): Goes beyond simply displaying information and visualizes connections between data. Additionally, we were impressed by the creative web page transitions and animations, as well as the aesthetically pleasing design

## Milestone 2 (7th May, 5pm)

**10% of the final grade**

[Milestone 2 report](https://github.com/com-480-data-visualization/project-2023-the-3-musketeers/docs/Data-viz-milestone-2.pdf)

[Our Website](https://com-480-data-visualization.github.io/project-2023-the-3-musketeers/)

## Milestone 3 (4th June, 5pm)

**80% of the final grade**


## Late policy

- < 24h: 80% of the grade for the milestone
- < 48h: 70% of the grade for the milestone

