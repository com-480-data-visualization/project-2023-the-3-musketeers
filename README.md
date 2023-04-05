# Project of Data Visualization (COM-480)

| Student's name | SCIPER |
| -------------- | ------ |
|Zhan Li |351592 |
| | |
| | |

[Milestone 1](#milestone-1) • [Milestone 2](#milestone-2) • [Milestone 3](#milestone-3)

## Milestone 1 (23rd April, 5pm)

**10% of the final grade**

This is a preliminary milestone to let you set up goals for your final project and assess the feasibility of your ideas.
Please, fill the following sections about your project.

*(max. 2000 characters per section)*

### Dataset

<!-- > Find a dataset (or multiple) that you will explore. Assess the quality of the data it contains and how much preprocessing / data-cleaning it will require before tackling visualization. We recommend using a standard dataset as this course is not about scraping nor data processing.
>
> Hint: some good pointers for finding quality publicly available datasets ([Google dataset search](https://datasetsearch.research.google.com/), [Kaggle](https://www.kaggle.com/datasets), [OpenSwissData](https://opendata.swiss/en/), [SNAP](https://snap.stanford.edu/data/) and [FiveThirtyEight](https://data.fivethirtyeight.com/)), you could use also the DataSets proposed by the ENAC (see the Announcements section on Zulip). -->

As Switzerland is especially famous for chocolate, we decided to explore the factors that play a role in deciding the quality of chocolate. The dataset we use for this project is [Chocolate Bar Ratings](https://www.kaggle.com/datasets/rtatman/chocolate-bar-ratings). The dataset records the ratings from experts of more than 1700 chocolate bars using. *Flavors of Cacao Rating System* is adopted to rate each chocolate from level Unpleasant (rating=1) to Elite (rating=5). This dataset also provides with us the background information (chocolate maker, specific bean origin, broad bean origin, REF value, review date, cocoa percentage, company location, date of review, cocoa percentage, company region and bean type). All the data are stored in a csv file of 1795 rows and 9 columns.  

### Problematic

> Frame the general topic of your visualization and the main axis that you want to develop.
> - What am I trying to show with my visualization?
> - Think of an overview for the project, your motivation, and the target audience.

### Exploratory Data Analysis

There are 1795 tuples in our dataset. Firstly, we check the first 5 rows of the data frame to get a first glimpse.

<img width="902" alt="image" src="https://user-images.githubusercontent.com/116460894/230116277-1d5af9df-978e-4a72-80b9-6f04ecfb0e1c.png">

Then we visualize some important variables to have some statistical insight.

![loc type](https://user-images.githubusercontent.com/116460894/230110520-6ef6dd69-b6ef-457c-84d8-92132cc1e3ca.jpg)

- the majority of the companies are from the US;
- however, the beans origins are mainly Central and South America;
- there is no type record for most of the beans, followed by the bean type Trinitario.

<img src="https://user-images.githubusercontent.com/116460894/230115519-dc578f9f-b8e7-4363-8502-267c7b2d3e80.jpg" alt="Cocoa Percent" width='500'><img src="https://user-images.githubusercontent.com/116460894/230112879-852d374c-d5c3-4cea-8f65-afcb3fdfc281.jpg" alt="Cocoa Percent vs  Rating" width=500>

- most of the chocolate bars reviewed contains 70% of cocoa;
- There's a slight negative correlation between Cocoa Percent and Rating.

### Related work


> - What others have already done with the data?
> - Why is your approach original?
> - What source of inspiration do you take? Visualizations that you found on other websites or magazines (might be unrelated to your data).
> - In case you are using a dataset that you have already explored in another context (ML or ADA course, semester project...), you are required to share the report of that work to outline the differences with the submission for this class.

## Milestone 2 (7th May, 5pm)

**10% of the final grade**


## Milestone 3 (4th June, 5pm)

**80% of the final grade**


## Late policy

- < 24h: 80% of the grade for the milestone
- < 48h: 70% of the grade for the milestone

