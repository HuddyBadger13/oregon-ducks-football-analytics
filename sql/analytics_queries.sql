.headers on
.mode column

SELECT
    COUNT(*) AS total_games,
    SUM(CASE WHEN result = 'W' THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN result = 'L' THEN 1 ELSE 0 END) AS losses,
    ROUND(
        100.0 * SUM(CASE WHEN result = 'W' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS win_percentage,
    ROUND(AVG(oregon_score), 2) AS average_points_scored,
    ROUND(AVG(opponent_score), 2) AS average_points_allowed,
    ROUND(AVG(margin), 2) AS average_margin
FROM games;