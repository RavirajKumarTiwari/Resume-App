# Tables in Resume App

**User**\
    -id\
    -username

**PersonalDatials**\
    - id\
    - name\
    - phone\
    - email\
    - address\
    - linkedin_url\
    - ForeighignKey('user.id')

**Experiences**\
    - id\
    - company_name\
    - role\
    - role_desc\
    - start_date\
    - end_date\
    - FroeignKey('user.id')

**Projects**\
    - id\
    - name\
    - desc\
    - start_date\
    - end_date\
    - ForeignKey('user.id')

**Skills**\
    - id\
    - title\
    - confidence_score\
    - ForeighKey('user.id')

**Education**\
    - id\
    - school_name\
    - degree\
    - start_date\
    - end_date\
    - ForeighKey('user.id')
