import React from "react"
import { IDeployErrorDialog } from "./types"

function UncommittedChanges(module: string): IDeployErrorDialog {
  return {
    title: "Are you sure you want to deploy this app?",
    body: (
      <>
        <p>
          The file <code>{module}</code> has uncommitted changes.
        </p>
        <p>Please commit the latest changes and push to GitHub to continue.</p>
      </>
    ),
  }
}

export default UncommittedChanges
