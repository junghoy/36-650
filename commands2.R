# Reading in text file

nba_teams <- read.table(file = "nba-teams.txt", sep="|", header=T)
nba_teams <- nba_teams[,-c(1,7)]


require("RPostgreSQL")

# create a connection
# save the password that we can "hide" it as best as we can by collapsing it
pw <- {
  "1dua234"
}

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
con <- dbConnect(drv, dbname = "postgres",
                 host = "localhost", port = 5432,
                 user = "postgres", password = pw)

# Write a table in our database
dbWriteTable(con, "teams", nba_teams, row.names = FALSE)

#To check that the table has been created
result <- dbSendQuery(con, "SELECT * from teams;")
dbFetch(result)
  

rm(pw) # removes the password
