![dvd_image](https://github.com/user-attachments/assets/e0b9c7f5-86f7-4fa6-a0aa-26c08bf8b66d)

A DVD rental company needs a model to predict how many days a customer will rent a DVD. Provided rental_info.csv contains features like rental and return dates, amount paid, movie details, and dummy variables for ratings. The goal is to build a robust model achieving an MSE ≤ 3 to support better inventory planning.

## 📂 Dataset: `rental_info.csv`

The dataset contains the following features:

| Column | Description |
|--------|-------------|
| `rental_date` | Date and time when the DVD was rented. |
| `return_date` | Date and time when the DVD was returned. |
| `amount` | Amount paid by the customer for renting the DVD. |
| `amount_2` | Square of the `amount`. |
| `rental_rate` | Rental rate of the DVD. |
| `rental_rate_2` | Square of the `rental_rate`. |
| `release_year` | Year the movie was released. |
| `length` | Length of the movie in minutes. |
| `length_2` | Square of the `length`. |
| `replacement_cost` | Cost of replacing the DVD. |
| `special_features` | Special features like trailers or deleted scenes. |
| `NC-17`, `PG`, `PG-13`, `R` | Dummy variables indicating the movie's rating. |
