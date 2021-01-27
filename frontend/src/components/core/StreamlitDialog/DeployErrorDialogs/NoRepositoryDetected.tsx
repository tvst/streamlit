import React from "react"
import { SHARING_DOCS_URL, TEAMS_URL } from "urls"
import { IDeployErrorDialog } from "./types"

function NoRepositoryDetected(): IDeployErrorDialog {
  return {
    title: "Unable to deploy app",
    body: (
      <>
        <p>Could not find a remote repository hosted on GitHub.</p>
        <p>How Streamlit sharing works:</p>
        <ul>
          <li>
            To deploy a public app, you must first put it in a public GitHub
            repo. See{" "}
            <a
              href={SHARING_DOCS_URL}
              rel="noopener noreferrer"
              target="_blank"
            >
              our documentation
            </a>{" "}
            for more details.
          </li>
          <li>
            If you'd like to deploy a private app,{" "}
            <a href={TEAMS_URL} target="_blank" rel="noopener noreferrer">
              sign up for Streamlit for Teams
            </a>
            .
          </li>
        </ul>
      </>
    ),
  }
}

export default NoRepositoryDetected
