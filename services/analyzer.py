import google.generativeai as genai

def analyze_resume(resume_text, job_title, job_description):
    model = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')
    prompt = f"""
Act as an expert resume analyst and career coach. You are analyzing a resume for a "{job_title}" position.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Please provide a structured analysis as follows:
Please follow the structure exactly and ensure all five sections are included in the response.


1. **Match Score**  
Provide only a numeric percentage indicating how well the resume matches the job description.  
Format: `85%` (No other text or explanation).

2. **Matching Skills/Keywords**  
List point-wise the specific skills or keywords that are present in both the resume and job description.

3. **Missing Skills/Keywords**  
List point-wise the important skills or keywords from the job description that are missing in the resume.

4. **Recommendations for Improvement**  
Provide 3 to 5 clear, actionable suggestions to improve this resume for this specific job application.

5. **ATS Optimization Score**  
Give a score between 0 and 100 indicating how well this resume is optimized for Applicant Tracking Systems (ATS).  

6. Justification: Also include 1–2 brief points justifying this score (e.g., keyword usage, formatting, etc.).

"""
    try:
        response = model.generate_content(prompt)
        print("Gemini response:", response.text)
        return response.text
    except Exception as e:
        return f"Error analyzing resume: {e}"


def ask_question_about_resume(resume_text, job_title, job_description, question):
    model = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')
    prompt = f"""
You are analyzing a resume for a {job_title} position.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

QUESTION: {question}

Please provide a clear and helpful answer based on the analysis.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"






# Provide a comprehensive analysis of the resume compared to the job requirements. Structure your analysis as follows:

# 1. Match Score: Provide a only percentage match score between the resume and job description no any other text want to percentage score.

# 4. Missing Skills/Keywords: give point vice only Identify specific skills or keywords from the job description that are missing in the resume.

# 4. Matching Skills/Keywords: give point vice only Identify specific skills or keywords from the job description that are matching in the resume.


# 2. Key Strengths: List 3-5 strengths in the resume that align well with the job requirements.

# 3. Improvement Areas: List 3-5 specific areas where the resume could be improved to better match the job.

# 4. Missing Skills/Keywords: Identify specific skills or keywords from the job description that are missing in the resume.

# 5. Format and Presentation: Analyze the structure, organization, and presentation of the resume.

# 6. Action Items: Provide 3-5 specific, actionable recommendations to improve the resume for this specific job application.
