-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE TOT_SCORE INT;
    DECLARE TOT_REC INT;
    SELECT SUM(score) INTO TOT_SCORE  FROM corrections WHERE user_id = user_id;
    SELECT COUNT(score) INTO TOT_REC FROM corrections WHERE user_id = user_id;
    IF TOT_SCORE IS NULL THEN
        UPDATE users SET average_score = 0 WHERE id = user_id;
    ELSE
        UPDATE users SET average_score = TOT_SCORE/TOT_REC WHERE id = user_id;
    END IF;
END$$