import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // file select
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  // drag drop
  const handleDrop = (event) => {
    event.preventDefault();

    const droppedFile = event.dataTransfer.files[0];

    if (droppedFile) {
      setFile(droppedFile);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  // click upload
  const handleClickUpload = () => {
    document.getElementById("fileInput").click();
  };

  // send resume to backend
const handleUpload = async () => {

  if (!file) {
    alert("Please upload a resume first");
    return;
  }

  setLoading(true);

  const formData = new FormData();
  formData.append("file", file);

  try {

    const response = await axios.post(
      "http://127.0.0.1:9000/upload-resume",
      formData
    );

    setResult(response.data);

  } catch (error) {

    console.error("Upload error:", error);

  }

  setLoading(false);
};

  return (

    <div className="container">

      <h1>AI Resume Analyzer</h1>

      <div
        className="upload-box"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onClick={handleClickUpload}
      >

        <p>Drag & Drop Resume Here</p>
        <p>or Click to Upload</p>

        <input
          id="fileInput"
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          style={{ display: "none" }}
        />

      </div>

      {file && <p>Selected file: {file.name}</p>}

      <button onClick={handleUpload}>
        Analyze Resume
      </button>
      {loading && (
  <div className="loading">
    <div className="spinner"></div>
    <p>Analyzing Resume...</p>
  </div>
)}

      {result && (

        <div style={{ marginTop: "30px" }}>

          <h2>Resume Score: {result.resume_score}%</h2>

          <h3>Skills Detected</h3>

          <div className="skill-container">

            {result.skills_detected.map((skill, index) => (
              <span key={index} className="skill-tag">
                {skill}
              </span>
            ))}

          </div>

          <h3>Missing Skills</h3>

          <div className="skill-container">

            {result.missing_skills.map((skill, index) => (
              <span key={index} className="skill-tag">
                {skill}
              </span>
            ))}

          </div>

          {result.job_matches && (

            <div>
              <h3>Resume Sections Found</h3>

              <div className="skill-container">

              {result.sections_found.map((section, index) => (
                <span key={index} className="skill-tag">
                 {section}
                </span>
               ))}

               </div>
          

              <h3>Recommended Jobs</h3>

              {result.job_matches.map((job, index) => (

                <div key={index} className="job-card">

                  <b>{job.job_role}</b>

                  <p>Match Score: {job.match_score}%</p>

                </div>

              ))}

            </div>

          )}
          {result.suggestions && (

  <div>

    <h3>Resume Improvement Suggestions</h3>

    {result.suggestions.map((tip, index) => (

      <div key={index} className="suggestion-card">

        {tip}

      </div>

    ))}

  </div>

)}

        </div>

      )}

    </div>

  );
}

export default App;