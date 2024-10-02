#HW2 Third Questions

## Question 4

def has_experience_as(CVS,job_title):
    users_with_experience = []
    for cv in CVS:
        if job_title in cv['jobs']:
            users_with_experience.append(cv['user'])
    return users_with_experience


## Question 5

def job_counts(CVS):
    job_count = {}
    for cv in CVS:
        for job in cv['jobs']:
            if job in job_count:
                job_count[job] += 1
            else:
                job_count[job] = 1
    return job_count


## Question 6


def most_popular_job(CVS):
    job_count = job_counts(CVS)
    max_count = 0
    for job, count in job_count.items():

        if count > max_count:
            most_popular = job
            max_count = count
            
    return (most_popular, max_count) 

