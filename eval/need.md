# 評估階段需要放入 `Data/` 的文件（need.md）

> 對應 `plan.md` v4.0 §2 與 Phase 0、Phase 4。缺少「必要」的文件，評估端會標 `NEEDS_HUMAN_INPUT` 並停在該關卡，不會自己補。
> 時間規則：**回答在 freeze 核准之後才生成**；`responses_round2/` 一次交齊 72 筆，重跑要附原因與紀錄，不要偷偷覆蓋。
> 欄位名稱是評估程式（`check_inputs.py`、`run_llm_judge.py`、`check_overlap.py`）實際會讀的名稱。

## 資料夾結構

```text
Data/
├── training/            # Ryan
├── retrieval/           # Shirley（Ryan 協助整理來源）
├── model/               # Shirley
├── responses_round2/    # Shirley：六組回答與 metadata（評估的主要輸入）
├── extra_conditions/    # 只有加入 GPT 規劃、review、重寫時才需要
└── round1_artifacts/    # Cian-Rong：第一輪與 judge 驗證用的舊資料（已有，集中放）
```

## 1. `Data/training/`（Ryan）

| 文件 | 必要 | 內容與格式 | 評估用途 |
|---|---|---|---|
| 最終 training file（例如 `train_vX_en.jsonl`） | 必要 | 現有 training schema；每筆有 `id`、`messages`（role / content）、`sources`（含 `url`）；固定版本後不再改 | 與 12 題做重疊檢查（`check_overlap.py`）；記錄 adapter 用的是哪一版 |
| manifest（`*.manifest.json`） | 必要 | 版本號、**總筆數、sha256**、每筆 id 與 hash、標籤（「AI-screened, with human spot checks」） | 版本可追溯（G1） |
| 候選／備用資料（reserve） | 有就放 | 同 training schema | 重疊檢查要一併涵蓋 |
| AI review 紀錄 | 必要 | 每筆的 keep / revise / reject、證據、原因、修改紀錄（review 分數與備註與 assistant 答案分開存） | 說明資料品質；不進 judge |
| 抽查紀錄 | 必要 | Ryan 隨機抽 15–20 筆的結果：id、family、回答或追問、是否安全題、核對的來源、發現的問題 | 報告用語要求「只有實際看過的才標 human-reviewed」 |
| 規則掃描或共通錯誤紀錄 | 有就放 | 例如 `RULE_SCAN_*.csv`、修改前後對照 | 解釋模型可能的缺點 |
| 資料分布與數量漏斗 | 必要 | 原始 drafts → 通過數 → 最終數；task family、情境類型、英文比例、官方來源數 | 報告資料說明 |
| 修改紀錄 | 必要 | 原始 ID 與修改前後文字、hash | 追溯 |

## 2. `Data/retrieval/`（Shirley，來源由 Ryan 協助整理）

| 文件 | 必要 | 內容與格式 | 評估用途 |
|---|---|---|---|
| active corpus | 必要 | 現有 loader 支援的 schema；每筆有穩定的 **document id**、操作正文、來源 URL、查閱日期、適用裝置／app／版本、必要前提 | judge 要讀檢索到的文字（轉成 `judge_docs.json`：id → 文字）；檢查 corpus 不含題目 |
| `corpus_manifest.json` | 必要 | 版本、筆數、sha256、新增與修訂清單 | G1 版本可追溯 |
| 來源缺口紀錄 | 必要 | 每個任務分三欄：「有相關文件」「文件足以支持完整操作」「缺少哪些步驟」 | 區分「來源不足」與「生成沒用好來源」 |
| 切分說明 | 必要 | 片段是否保留前提與相鄰步驟、適用範圍與安全提示是否隨片段取出 | 解釋「步驟只出現一半」的情況 |
| loader 與驗證輸出 | 必要 | 現有程式讀取新 records 的結果（來源、必填 metadata、ID 唯一性） | 確認用的是 active corpus，沒讀 archive |
| retriever 設定 | 必要 | 方法（例如 BM25）、top-k、切分大小、是否用裝置過濾；B3 與 PT+R **必須相同** | 公平比較 |

規則：corpus 可以放與測試任務相關的一般官方文件，**不可放測試題、參考答案或 `expected_elements`**。

## 3. `Data/model/`（Shirley）

| 文件 | 必要 | 內容與格式 | 評估用途 |
|---|---|---|---|
| 訓練紀錄 | 必要 | 使用的**訓練檔版本與 sha256**、epochs、learning rate、LoRA 設定、seed、steps、batch size、gradient accumulation、精度、環境版本（Python、torch、transformers、peft 等） | 每個 adapter 都要能對應到訓練資料版本 |
| adapter metadata | 必要 | adapter 名稱、對應的 base 模型、checkpoint 路徑（**只記 metadata，不放權重**） | 回答 log 回溯 |
| 舊 20 筆 checkpoint 紀錄 | 必要 | 名稱、訓練資料、日期 | 第一輪舊結果的說明；不與新結果混算 |
| 小批次驗證紀錄 | 必要 | prompt 與 assistant 目標是否正確、loss 設定、角色、完整對話 token 數、最長樣本、adapter 載入結果；發現問題的修正說明 | 確認模型確實學到完整示範 |
| 訓練 max-length | 必要 | 訓練上限（768）與是否有樣本被截斷的檢查結果 | 與生成時 `max_new_tokens` 分開記錄 |

## 4. `Data/responses_round2/`（Shirley）：最重要

| 文件 | 必要 | 內容與格式 | 評估用途 |
|---|---|---|---|
| **六組回答檔**（一組一個 `.jsonl`） | 必要 | 每題一行，欄位：`scenario_id`、`response`（或 `response_text`）；建議另附 `response_id`（唯一）、`condition`、`run_id`、`truncated`（true / false）；RAG 組另有 `retrieval.document_ids`（陣列）。**12 題 × 6 組 = 72 筆，每組每題恰好一筆** | `check_inputs.py`、`run_llm_judge.py` 直接讀 |
| `conditions.json` | 必要 | `{"組別名": "檔名.jsonl", ...}`；組別名要和 `decision_v4_rule.md` §9 的配對一致（預設 B0、B1、B2、B3、PT、PT+R） | 評分與分析的組別對照 |
| `id_map`（條件對照，**私有**） | 必要 | `scenario_id`、`response_id`、`condition`、`adapter`、`run_id`；**不給 judge 與人工評分者** | 評完才解盲 |
| **實際模型輸入 log**（例如 `model_inputs.jsonl`） | 必要 | 每題每組：實際送進 router／生成器的 system message、使用者對話、檢索文字、route 決策（answer / clarify / insufficient） | **標籤洩漏檢查**：不得出現 `expected_elements`、`clarification_required`、`notes_for_raters`，也不得用評估題 ID 查表 |
| 檢索紀錄 | 必要（B3、PT+R） | 每題：檢索到的 document id、順序、分數、corpus 版本、來源 URL、裝置標籤是否匹配 | 判斷「檢索不足」與「沒用好檢索內容」；與 `judge_docs.json` 對照 |
| run 設定 | 必要 | 每組：基礎模型、adapter（或無）、system prompt 檔與 hash、decoding（temperature、greedy 與否、seed）、`max_new_tokens`（768）、日期、執行環境、commit | 可重現、公平比較 |
| 截斷紀錄 | 必要 | 每組：哪些回答碰到長度上限（例如 `*.summary.json` 的 `hit_length_limit_ids`），或每筆 `truncated` | 截斷的回答要標示 |
| 輸出檔 sha256 | 必要 | 每個回答檔的 sha256 | 證明評分後檔案沒被改 |
| 重跑紀錄 | 有重跑就必要 | 重跑原因、原始檔保留 | 不靜默覆蓋 |

## 5. `Data/extra_conditions/`（只有加入額外條件才需要）

若加入 GPT 線上規劃、review 或重寫：另放一組回答檔，格式同 §4，另加：使用的模型與版本、完整 prompt、成本（token 與費用）、延遲、哪一步由強模型完成。這一組**不進主表六組**，報告另列。

## 6. `Data/round1_artifacts/`（Cian-Rong；多數已經有）

| 文件 | 位置 | 用途 |
|---|---|---|
| `eval_v1.jsonl`（15 題）與 `scenario_prep_v2.json` | `eval/` | 用第一輪驗證 judge |
| 三組舊回答（original、prompt、sft）與後來的 sft_v2、RAG、v6 回答 | `testing` branch 的 `eval/outputs/` | judge 驗證與開發集結果 |
| 舊 judge 原始結果 | `eval/judge_out/`、`eval/judge_out_v4/` | 驗證與稽核；不是只給平均分數表 |
| 真人 pilot 與 8 筆驗證 | `eval/human_validation_*`、pilot 評分檔 | 既有人工證據 |
| `audit_v1`、`routing_audit` | 需 Shirley 或 Ryan 提供位置 | 第一輪稽核；**目前我不確定這兩個檔案在哪裡**，需要確認 |
欄位名稱（scenario_id、response、retrieval.document_ids、truncated） check_inputs.py 評估程式實際會讀的名稱 (請 Shirley 照這個格式輸出)

## 7. 評估端自己產生（不用放進 `Data/`，列出來避免漏掉）

12 題 `eval_v2.jsonl` 與只含 prompt 的檔案、`scenario_prep_v3.json`、`judge_docs.json`、`freeze_manifest.json`、judge 輸出、稽核與分析檔，都在 `eval/round2/`。

## 8. 交件前自我檢查（Shirley 與 Ryan 各自勾）

- [ ] 所有檔案都標了版本與 sha256，能對應到 `plan.md` 的 G1。
- [ ] 回答檔剛好 72 筆（或組數 × 12），沒有重複、沒有缺題。
- [ ] 回答是用 **`eval_v2_prompts_only.jsonl`** 生成的，沒有使用任何評估標籤。
- [ ] 模型輸入 log 是**真實送進模型的內容**，不是事後整理的。
- [ ] B3 與 PT+R 用同一個 corpus、同一個 retriever 設定。
- [ ] 沒有中文字出現在英文題的回答裡（有的話寫明原因）。
- [ ] corpus 沒有題目文字、參考答案或 `expected_elements`。
- [ ] 沒有 API 金鑰、token、個資在任何檔案裡。
- [ ] 沒在看過評分後再調整系統；若有調整，標成新版本並重新生成。

hint
按提供者分成4個資料夾，每個資料夾列出必要文件、格式或欄位、評估端怎麼用：

Data/training/（Ryan）： 最終 training file 與 manifest（版本、筆數、sha256）、AI review 紀錄、抽查紀錄、資料分布與漏斗、修改紀錄。

Data/retrieval/（Shirley）： active corpus（含 document id、來源、適用裝置版本）、corpus manifest、來源缺口紀錄、切分說明、loader 驗證輸出、retriever 設定（B3 與 PT+R 要相同）。
Data/model/（Shirley）： 訓練紀錄（含訓練檔版本與 sha256）、adapter metadata、舊 20 筆 checkpoint 紀錄、小批次驗證紀錄。
Data/responses_round2/（Shirley，最重要）：
六組回答檔，12 題 × 6 組 = 72 筆。
conditions.json、私有的 id_map。
實際模型輸入 log、檢索紀錄、run 設定、截斷紀錄、輸出檔 sha256。


最後有一份交件前自我檢查清單，例如：用 prompts-only 檔生成、沒有使用評估標籤、corpus 不含題目。

有兩點要你注意：

第六節「第一輪資料」我寫了 audit_v1 和 routing_audit，這是團隊規劃裡提到的檔名，但我在資料夾裡找不到這兩個檔案，也不確定在哪裡。需要問 Ryan 或 Shirley，我在檔案裡也這樣標註了。
欄位名稱（scenario_id、response、retrieval.document_ids、truncated）是我寫的評估程式實際會讀的名稱，請 Shirley 照這個格式輸出，否則 check_inputs.py 會失敗。