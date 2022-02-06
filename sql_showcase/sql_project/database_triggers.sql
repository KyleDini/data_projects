-- TRIGGERS:

-- Note: its much easier to accomplish most of what triggers in sql do with other coding languages.
-- Note: Triggers can make debugging hard! They usually happen behind the scenes and are hard to find/easily forgotten. To many triggers/chaining triggers can also cause issues.

-- SYNTAX:
CREATE TRIGGER trigger_name
    trigger_time trigger_event ON table_name FOR EACH ROW
    BEGIN
    ...
    END
;

-- LISTING TRIGGERS:
SHOW TRIGGERS;

-- REMOVING TRIGGERS:
DROP TRIGGER trigger_name;

-- TRIGGER TIME: BEFORE, AFTER
-- TRIGGER EVENT: INSERT, UPDATE, DELETE
-- ^ ON TABLE_NAME

-- USES: 
-- Validating data (Ex: someone can only sign up for a website if they're 18 or older), easier to just write code to do this in other languages most of the time
-- Manipulating other tables based off a trigger(Ex: Unfollowing someone on IG, adds that unfollow to a table to keep track of total unfollows)

-- 18 OR OLDER EXAMPLE:
DELIMITER $$

CREATE TRIGGER must_be_adult
     BEFORE INSERT ON people FOR EACH ROW
     BEGIN
          IF NEW.age < 18
          THEN
              SIGNAL SQLSTATE '45000'
              -- SQLSTATE 45000 is a generic error state that represents "unhandled user-defined exceptions"
                    SET MESSAGE_TEXT = 'Must be an adult!';
          END IF;
     END;
$$

DELIMITER ;
-- DELIMITER LETS YOU RUN BLOCKS OF CODE THAT HAVE MULTIPLE SEMI-COLONS IN SQL 

--  PREVENT USERS FROM FOLLOWING THEMSELVES EXAMPLE:
DELIMITER $$

CREATE TRIGGER example_cannot_follow_self
     BEFORE INSERT ON follows FOR EACH ROW
     BEGIN
          IF NEW.follower_id = NEW.followee_id
          THEN
               SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Cannot follow yourself!';
          END IF;
     END;
$$

DELIMITER ;

-- LOGGING UNFOLLOWS EXAMPLE:
DELIMITER $$

CREATE TRIGGER create_unfollow
    AFTER DELETE ON follows FOR EACH ROW 
BEGIN
    INSERT INTO unfollows
    SET follower_id = OLD.follower_id,
        followee_id = OLD.followee_id;
END$$

DELIMITER ;