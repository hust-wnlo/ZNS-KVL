The Trace file implements content related to workload analysis.
The zns file implements the content of the three modules in ZNS-KVL.

All files can be installed and run in the emulator through plugins.


ZNS-KVL consists of three modules: 1) The attention-aware zone allocator uses Transformer attention weights to implement semantic-level hot/cold tiering and map it to ZNS physical zones. 2) The task-driven scheduler dynamically adjusts internal SSD activities based on the characteristics of different stages of inference. 3) A cluster-based cache prefetcher implements adaptive prefetching by analyzing the characteristics of address clusters through a clustering process.

