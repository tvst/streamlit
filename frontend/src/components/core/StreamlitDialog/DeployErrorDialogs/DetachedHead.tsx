import React from "react"
import { IDeployErrorDialog } from "./types"

function DetachedHead(): IDeployErrorDialog {
  return {
    title: "Are you sure you want to deploy this app?",
    body: (
      <>
        <p>This Git tree is in a detached HEAD state.</p>
        <p>Please commit the latest changes and push to GitHub to continue.</p>
      </>
    ),
  }
}

export default DetachedHead
