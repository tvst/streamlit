/**
 * @license
 * Copyright 2018-2020 Streamlit Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React, { PureComponent, ReactNode } from "react"
import DeckGL from "deck.gl"
import Immutable from "immutable"
import { StaticMap } from "react-map-gl"
import * as layers from "@deck.gl/layers"
import { JSONConverter } from "@deck.gl/json"
import * as aggregationLayers from "@deck.gl/aggregation-layers"

import { CSVLoader } from "@loaders.gl/csv"
import { registerLoaders } from "@loaders.gl/core"

import withFullScreenWrapper from "hocs/withFullScreenWrapper"

import "mapbox-gl/dist/mapbox-gl.css"
import "./DeckGlJsonChart.scss"

interface PickingInfo {
  object: {
    [key: string]: string
  }
}

interface DeckObject {
  initialViewState: {
    height: number
    width: number
  }
  layers: Array<object>
  mapStyle?: string | Array<string>
}

const configuration = {
  classes: { ...layers, ...aggregationLayers },
}

registerLoaders([CSVLoader])

const jsonConverter = new JSONConverter({ configuration })

const MAPBOX_ACCESS_TOKEN =
  "pk.eyJ1IjoidGhpYWdvdCIsImEiOiJjamh3bm85NnkwMng4M3dydnNveWwzeWNzIn0.vCBDzNsEF2uFSFk2AM0WZQ"

export interface Props {
  width: number
  element: Immutable.Map<string, any>
}

interface PropsWithHeight extends Props {
  height: number | undefined
}

interface State {
  initialized: boolean
}

export class DeckGlJsonChart extends PureComponent<PropsWithHeight, State> {
  static defaultProps = {
    height: 500,
  }

  state = {
    initialized: false,
  }

  componentDidMount = (): void => {
    // HACK: Load layers a little after loading the map, to hack around a bug
    // where HexagonLayers were not drawing on first load but did load when the
    // script got re-executed.
    this.setState({
      initialized: true,
    })
  }

  fixHexLayerBug = (): void => {
    this.setState({ initialized: true })
  }

  getDeckObject = (): DeckObject => {
    const { element, width, height } = this.props
    const json = JSON.parse(element.get("json"))

    json.initialViewState.height = height
    json.initialViewState.width = width

    delete json.views // We are not using views. This avoids a console warning.

    return jsonConverter.convert(json)
  }

  createTooltip = (info: PickingInfo): object | boolean => {
    const { element } = this.props
    let tooltip = element.get("tooltip")

    if (!info || !info.object || !tooltip) {
      return false
    }

    tooltip = JSON.parse(tooltip)

    const matchedVariables = tooltip.html.match(/{(.*?)}/g)

    if (matchedVariables) {
      matchedVariables.forEach((el: string) => {
        const variable = el.substring(1, el.length - 1)

        if (info.object[variable]) {
          tooltip.html = tooltip.html.replace(el, info.object[variable])
        }
      })
    }

    return tooltip
  }

  render(): ReactNode {
    const deck = this.getDeckObject()

    return (
      <div
        className="stDeckGlJsonChart"
        style={{
          height: deck.initialViewState.height,
          width: deck.initialViewState.width,
        }}
      >
        <DeckGL
          initialViewState={deck.initialViewState}
          height={deck.initialViewState.height}
          width={deck.initialViewState.width}
          layers={this.state.initialized ? deck.layers : []}
          getTooltip={this.createTooltip}
          controller
        >
          <StaticMap
            height={deck.initialViewState.height}
            width={deck.initialViewState.width}
            mapStyle={
              deck.mapStyle
                ? typeof deck.mapStyle === "string"
                  ? deck.mapStyle
                  : deck.mapStyle[0]
                : undefined
            }
            mapboxApiAccessToken={MAPBOX_ACCESS_TOKEN}
          />
        </DeckGL>
      </div>
    )
  }
}

export default withFullScreenWrapper(DeckGlJsonChart)
