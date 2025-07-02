from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Personal Information
    personal_info = {
        "name": "Sai Manohar Boidapu",
        "location": "Bengaluru, India",
        "phone": "+91 9686239385",
        "email": "boidapu.manohar@gmail.com",
        "linkedin": "https://linkedin.com/in/sai-manohar-boidapu"
    }

    # Resume Data
    professional_summary = (
        "Innovative and strategic Data Engineering Leader with 11 years of experience designing and "
        "implementing modern data architecture, leading cross-functional teams, and driving data-centric solutions. "
        "Expertise in Big Data, distributed systems, and cloud technologies (AWS, Snowflake, Kubernetes). "
        "Recognized for fostering innovation, achieving measurable outcomes, and delivering end-to-end data solutions."
    )

    skills = {
        "Leadership & Management": [
            "Team Leadership", "Mentorship", "Stakeholder Collaboration", 
            "Agile Practices", "Strategic Planning", "Communication", 
            "Critical Thinking", "Decision Making", "Capacity Planning"
        ],
        "Technical Expertise": [
            "Data Engineering", "Platform Architecture", "DevSecOps", 
            "CI/CD", "Cloud Platforms (AWS)", "Data Warehousing (Snowflake, Redshift)", 
            "ETL Pipelines", "Microservices"
        ],
        "Programming & Tools": [
            "Python", "SQL", "Java", "Apache Spark", "Airflow", 
            "DBT", "Kafka", "Datadog"
        ],
        "Technologies": [
            "Hadoop Ecosystem (Hive, Pig, Sqoop)", "REST APIs", 
            "Data Visualization", "Kubernetes (AWS EKS)"
        ]
    }

    experience = [
        {
            "title": "Technical Lead (Senior Data Engineer)",
            "company": "Pluralsight",
            "location": "Bengaluru, India",
            "duration": "Jan 2023 – Present",
            "details": [
                "Managed cross-functional teams of 10+ engineers.",
                "Architected modern data platforms using AWS, Spark, Materialize, DBT, Kafka, Snowflake, and Kubernetes.",
                "Optimized ETL pipelines, increasing efficiency by 30% and reducing latency by 40%."
            ]
        },
        # Additional experiences omitted for brevity
    ]

    education = [
        {
            "degree": "Bachelor of Technology in Computer Science and Engineering",
            "institution": "Raghu Engineering College",
            "location": "Visakhapatnam, India",
            "year": "2010 – 2014"
        }
    ]

    leadership = [
        "Winner, Skillenza Kreate Hackathon – 2019",
        "Finalist, Tech Sparks Hackathon – 2015"
    ]

    additional = {
        "Languages": ["English", "Hindi", "Telugu"],
        "Certifications": ["Oracle Cloud Infrastructure 2024 Generative AI Professional (1Z0-1127-24)"]
    }

    return render_template(
        'resume.html',
        personal_info=personal_info,
        professional_summary=professional_summary,
        skills=skills,
        experience=experience,
        education=education,
        leadership=leadership,
        additional=additional
    )

if __name__ == '__main__':
    app.run(debug=True)
