-- specific test to check that GENRES column in MOVIES_SERIES_SHARE is not null
SELECT * FROM {{ ref('MOVIES_SERIES_SHARE') }} WHERE GENRES IS NULL