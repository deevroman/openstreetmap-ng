export interface OSMNode {
    type: "node"
    id: bigint
    geom: [number, number]
    version?: bigint
}

export interface OSMWay {
    type: "way"
    id: bigint
    geom: [number, number][]
    version?: bigint
    area?: boolean
}

export interface OSMRelation {
    type: "relation"
    id: bigint
    version?: bigint
}

export interface OSMNote {
    type: "note"
    id?: bigint
    geom: [number, number]
    text: string
    status: "open" | "closed" | "hidden"
}

/** [minLon, minLat, maxLon, maxLat] */
export type Bounds = [number, number, number, number]

export interface OSMChangeset {
    type: "changeset"
    id: bigint
    bounds: Bounds[]
}

export type OSMObject = OSMNode | OSMWay | OSMRelation | OSMNote | OSMChangeset
