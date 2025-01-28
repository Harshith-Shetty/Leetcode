/* Write your T-SQL query statement below */
With cte as  (
    Select  tiv_2016 ,
            count(*) over(PARTITION  by tiv_2015) as count_tiv_2015,
            count(*) over(PARTITION  by lat, lon) as count_lan_lon
    from Insurance
)
Select Round(Sum(tiv_2016),2) as tiv_2016 FROM cte WHERE count_tiv_2015 > 1 and count_lan_lon = 1