import * as OBC from "@thatopen/components";
import type { ViewerConfig } from "./config";

export async function loadModelFromUrl(
  ifcLoader: OBC.IfcLoader,
  url: string,
  name?: string,
): Promise<void> {
  const modelName =
    name ?? url.split("/").pop()?.replace(".ifc", "") ?? "model";

  console.log(`[PyNET Viewer] Loading: ${modelName} from ${url}`);

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: ${response.status}`);
  }

  const buffer = await response.arrayBuffer();
  const bytes = new Uint8Array(buffer);
  await ifcLoader.load(bytes, true, modelName);

  console.log(`[PyNET Viewer] Loaded: ${modelName}`);
}

export async function loadAllModels(
  config: ViewerConfig,
  ifcLoader: OBC.IfcLoader,
  onProgress?: (loaded: number, total: number, name: string) => void,
): Promise<void> {
  const total = config.modelUrls.length;
  for (let i = 0; i < total; i++) {
    const url = config.modelUrls[i];
    const name = url.split("/").pop()?.replace(".ifc", "") ?? `model-${i}`;
    onProgress?.(i, total, name);
    await loadModelFromUrl(ifcLoader, url, name);
  }
  onProgress?.(total, total, "done");
}
