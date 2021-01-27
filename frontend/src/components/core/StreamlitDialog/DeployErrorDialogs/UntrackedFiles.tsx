import React from "react"
import { IDeployErrorDialog } from "./types"

function UntrackedFiles(): IDeployErrorDialog {
  return {
    title: "Are you sure you want to deploy this app?",
    body: (
      <>
        <p>
          This Git repo has untracked files. You may want to commit them and
          push to GitHub before continuing.
        </p>
        <p>
          Alternatively, you can either delete the files (if they're not
          needed) or add them to your <code>.gitignore</code>.
        </p>
      </>
    ),
  }
}

export default UntrackedFiles
