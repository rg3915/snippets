SELECT
    s.id, s.tstamp, s.value,
    IFNULL(value - (SELECT
        mt.diferenca
        FROM diferenca mt
        WHERE mt.id < m.id
        ORDER BY mt.id
        DESC LIMIT 0,1), 0) AS variation
    FROM sale s
    WHERE s.user_id = 1;