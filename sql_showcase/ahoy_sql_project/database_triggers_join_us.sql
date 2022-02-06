-- SYNTAX:
CREATE TRIGGER trigger_name
    trigger_time trigger_event ON table_name FOR EACH ROW
    BEGIN
    ...
    END
;

-- TRIGGER TIME: BEFORE, AFTER
-- TRIGGER EVENT: INSERT, UPDATE, DELETE
-- ^ ON TABLE_NAME