import React from "react"
import { IDeployErrorDialog } from "./types"

function RepoIsAhead(): IDeployErrorDialog {
  return {
    title: "Are you sure you want to deploy this app?",
    body: (
      <>
        <p>
          This Git repo has uncommitted changes. You may want to commit them
          and push to GitHub before continuing.
        </p>
      </>
    ),
  }
}

export default RepoIsAhead
