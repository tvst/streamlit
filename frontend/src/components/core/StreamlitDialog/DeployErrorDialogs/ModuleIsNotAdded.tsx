import React from "react"
import { IDeployErrorDialog } from "./types"

function ModuleIsNotAdded(module: string): IDeployErrorDialog {
  return {
    title: "Unable to deploy app",
    body: (
      <>
        <p>
          This application's main file, <code>{module}</code>, is not being
          tracked in this Git repo.
        </p>
        <p>Please commit it and push to GitHub, then try again.</p>
      </>
    ),
  }
}

export default ModuleIsNotAdded
