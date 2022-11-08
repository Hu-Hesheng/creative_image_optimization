CREATE TABLE IF NOT EXISTS `score_table` 
(
    'ER': 'FLOAT NOT NULL',
    'CTR': 'FLOAT NOT NULL',
    -- 'all_text': 'FLOAT NOT NULL',
    'LAR': 'FLOAT DEFAULT NULL',
    'all_objects_count': 'INT DEFAULT NULL',
    'unique_objects_count': 'INT DEFAULT NULL',
    -- 'cta_text': 'INT DEFAULT NULL'
    'cta_width': 'FLOAT DEFAULT NULL'
    'cta_height' : 'FLOAT DEFAULT NULL'
    

    -- PRIMARY KEY (`user_id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;