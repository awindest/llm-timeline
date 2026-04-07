<script lang="ts">
	import { colors, typography, space, radius, shadow } from '$lib/styles/tokens';

	interface LLM {
		name: string;
		nameLink: string;
		date: string;
		developer: string;
		developerLink: string;
		parameters: string;
		corpus: string;
		cost: string;
		notes: string;
	}

	const DATA: LLM[] = [
		{
			name: 'GPT-1',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-1',
			date: '2018-06-11',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: '0.117',
			corpus: 'Unknown',
			cost: '1',
			notes: 'First GPT model, decoder-only transformer. Trained for 30 days on 8 P600 GPUs.'
		},
		{
			name: 'BERT',
			nameLink: 'https://en.wikipedia.org/wiki/BERT_(language_model)',
			date: '2018-10-01',
			developer: 'Google',
			developerLink: 'https://en.wikipedia.org/wiki/Google',
			parameters: '0.340',
			corpus: '3.3 billion words',
			cost: '9',
			notes:
				'An early and influential language model. Encoder-only and thus not built to be prompted or generative. Training took 4 days on 64 TPUv2 chips.'
		},
		{
			name: 'T5',
			nameLink: 'https://en.wikipedia.org/wiki/T5_(language_model)',
			date: '2019-10-01',
			developer: 'Google',
			developerLink: '',
			parameters: '11',
			corpus: '34 billion tokens',
			cost: '',
			notes: 'Base model for many Google projects, such as Imagen.'
		},
		{
			name: 'XLNet',
			nameLink: 'https://en.wikipedia.org/wiki/XLNet',
			date: '2019-06-01',
			developer: 'Google',
			developerLink: '',
			parameters: '0.340',
			corpus: '33 billion words',
			cost: '330',
			notes:
				'An alternative to BERT; designed as encoder-only. Trained on 512 TPU v3 chips for 5.5 days.'
		},
		{
			name: 'GPT-2',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-2',
			date: '2019-02-01',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: '1.5',
			corpus: '40GB (~10 billion tokens)',
			cost: '28',
			notes: 'Trained on 32 TPUv3 chips for 1 week.'
		},
		{
			name: 'GPT-3',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-3',
			date: '2020-05-01',
			developer: 'OpenAI',
			developerLink: '',
			parameters: '175',
			corpus: '300 billion tokens',
			cost: '3640',
			notes:
				'A fine-tuned variant of GPT-3, termed GPT-3.5, was made available to the public through a web interface called ChatGPT in 2022.'
		},
		{
			name: 'GPT-Neo',
			nameLink: '',
			date: '2021-03-01',
			developer: 'EleutherAI',
			developerLink: 'https://en.wikipedia.org/wiki/EleutherAI',
			parameters: '2.7',
			corpus: '825 GiB',
			cost: 'Unknown',
			notes:
				'The first of a series of free GPT-3 alternatives released by EleutherAI. GPT-Neo outperformed an equivalent-size GPT-3 model on some benchmarks, but was significantly worse than the largest GPT-3.'
		},
		{
			name: 'GPT-J',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-J',
			date: '2021-06-01',
			developer: 'EleutherAI',
			developerLink: '',
			parameters: '6',
			corpus: '825 GiB',
			cost: '200',
			notes: 'GPT-3-style language model trained on The Pile.'
		},
		{
			name: 'Megatron-Turing NLG',
			nameLink: '',
			date: 'October 2021',
			developer: 'Microsoft and Nvidia',
			developerLink: '',
			parameters: '530',
			corpus: '338.6 billion tokens',
			cost: '38000',
			notes:
				'Trained for 3 months on over 2000 A100 GPUs on the NVIDIA Selene Supercomputer, for over 3 million GPU-hours.'
		},
		{
			name: 'Ernie 3.0 Titan',
			nameLink: '',
			date: '2021-12-01',
			developer: 'Baidu',
			developerLink: 'https://en.wikipedia.org/wiki/Baidu',
			parameters: '260',
			corpus: '4TB',
			cost: 'Unknown',
			notes: 'Chinese-language LLM initially used by Ernie Bot.'
		},
		{
			name: 'Claude',
			nameLink: '',
			date: '2021-12-01',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: '52',
			corpus: '400 billion tokens',
			cost: 'Unknown',
			notes: 'Fine-tuned for desirable behavior in conversations.'
		},
		{
			name: 'GLaM',
			nameLink: '',
			date: '2021-12-01',
			developer: 'Google',
			developerLink: 'https://en.wikipedia.org/wiki/Google',
			parameters: '1200',
			corpus: '1.6 trillion tokens',
			cost: '5600',
			notes:
				'Sparse mixture of experts (MoE) model, making it more expensive to train but cheaper to run inference compared to GPT-3.'
		},
		{
			name: 'Gopher',
			nameLink: '',
			date: '2021-12-01',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: '280',
			corpus: '300 billion tokens',
			cost: '5833',
			notes: 'Later developed into the Chinchilla model.'
		},
		{
			name: 'LaMDA',
			nameLink: 'https://en.wikipedia.org/wiki/LaMDA',
			date: '2022-01-01',
			developer: 'Google',
			developerLink: '',
			parameters: '137',
			corpus: '1.56T words, 168 billion tokens',
			cost: '4110',
			notes: 'Specialized for response generation in conversations.'
		},
		{
			name: 'GPT-NeoX',
			nameLink: '',
			date: '2022-02-01',
			developer: 'EleutherAI',
			developerLink: 'https://en.wikipedia.org/wiki/EleutherAI',
			parameters: '20',
			corpus: '825 GiB',
			cost: '740',
			notes: 'Based on the Megatron architecture.'
		},
		{
			name: 'Chinchilla',
			nameLink: 'https://en.wikipedia.org/wiki/Chinchilla_AI',
			date: '2022-03-01',
			developer: 'Google DeepMind',
			developerLink: '',
			parameters: '70',
			corpus: '1.4 trillion tokens',
			cost: '6805',
			notes:
				'Reduced-parameter model trained on more data. Used in the Sparrow bot. Often cited for its neural scaling law.'
		},
		{
			name: 'PaLM',
			nameLink: 'https://en.wikipedia.org/wiki/PaLM',
			date: '2022-04-01',
			developer: 'Google',
			developerLink: '',
			parameters: '540',
			corpus: '768 billion tokens',
			cost: '29250',
			notes: 'Trained for ~60 days on ~6000 TPU v4 chips.'
		},
		{
			name: 'OPT',
			nameLink: '',
			date: '2022-05-01',
			developer: 'Meta',
			developerLink: 'https://en.wikipedia.org/wiki/Meta_Platforms',
			parameters: '175',
			corpus: '180 billion tokens',
			cost: '310',
			notes:
				'GPT-3 architecture with some adaptations from Megatron. The training logbook written by the team was published.'
		},
		{
			name: 'YaLM 100B',
			nameLink: '',
			date: '2022-06-01',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: '100',
			corpus: '1.7TB',
			cost: 'Unknown',
			notes: "English-Russian model based on Microsoft's Megatron-LM."
		},
		{
			name: 'Minerva',
			nameLink: '',
			date: '2022-06-01',
			developer: 'Google',
			developerLink: 'https://en.wikipedia.org/wiki/Google',
			parameters: '540',
			corpus: '38.5B tokens from mathematical webpages and arXiv',
			cost: 'Unknown',
			notes:
				'For solving mathematical and scientific questions using step-by-step reasoning. Initialized from PaLM models.'
		},
		{
			name: 'BLOOM',
			nameLink: 'https://en.wikipedia.org/wiki/BLOOM_(language_model)',
			date: '2022-07-01',
			developer: 'Large collaboration led by Hugging Face',
			developerLink: 'https://en.wikipedia.org/wiki/Hugging_Face',
			parameters: '175',
			corpus: '350 billion tokens (1.6TB)',
			cost: 'Unknown',
			notes:
				'Essentially GPT-3 but trained on a multi-lingual corpus (30% English excluding programming languages).'
		},
		{
			name: 'Galactica',
			nameLink: '',
			date: '2022-11-01',
			developer: 'Meta',
			developerLink: '',
			parameters: '120',
			corpus: '106 billion tokens',
			cost: 'Unknown',
			notes: 'Trained on scientific text and modalities.'
		},
		{
			name: 'AlexaTM',
			nameLink: '',
			date: '2022-11-01',
			developer: 'Amazon',
			developerLink: 'https://en.wikipedia.org/wiki/Amazon_(company)',
			parameters: '20',
			corpus: '1.3 trillion',
			cost: 'Unknown',
			notes: 'Uses a bidirectional sequence-to-sequence architecture.'
		},
		{
			name: 'Llama',
			nameLink: 'https://en.wikipedia.org/wiki/Llama_(language_model)',
			date: '2023-02-01',
			developer: 'Meta AI',
			developerLink: 'https://en.wikipedia.org/wiki/Meta_AI',
			parameters: '65',
			corpus: '1.4 trillion',
			cost: '6300',
			notes:
				'Corpus has 20 languages. Overtrained (compared to the Chinchilla scaling law) for better performance with fewer parameters.'
		},
		{
			name: 'GPT-4',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-4',
			date: '2023-03-01',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Now available for all ChatGPT users; used in several products.'
		},
		{
			name: 'Cerebras-GPT',
			nameLink: '',
			date: '2023-03-01',
			developer: 'Cerebras',
			developerLink: 'https://en.wikipedia.org/wiki/Cerebras',
			parameters: '13',
			corpus: '',
			cost: '270',
			notes: 'Trained with the Chinchilla neural scaling formula.'
		},
		{
			name: 'Falcon',
			nameLink: '',
			date: '2023-03-01',
			developer: 'Technology Innovation Institute',
			developerLink: 'https://en.wikipedia.org/wiki/Technology_Innovation_Institute',
			parameters: '40',
			corpus: '1 trillion tokens from RefinedWeb plus curated corpora',
			cost: '2800',
			notes: ''
		},
		{
			name: 'BloombergGPT',
			nameLink: '',
			date: '2023-03-01',
			developer: 'Bloomberg L.P.',
			developerLink: 'https://en.wikipedia.org/wiki/Bloomberg_L.P.',
			parameters: '50',
			corpus: '363B tokens proprietary + 345B general purpose',
			cost: 'Unknown',
			notes: 'Designed for financial tasks.'
		},
		{
			name: 'PanGu-Σ',
			nameLink: 'https://en.wikipedia.org/wiki/Huawei_PanGu',
			date: '2023-03-01',
			developer: 'Huawei',
			developerLink: 'https://en.wikipedia.org/wiki/Huawei',
			parameters: '1085',
			corpus: '329 billion tokens',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'OpenAssistant',
			nameLink: 'https://en.wikipedia.org/wiki/List_of_large_language_models',
			date: '2023-03-01',
			developer: 'LAION',
			developerLink: 'https://en.wikipedia.org/wiki/LAION',
			parameters: '17',
			corpus: '1.5 trillion tokens',
			cost: 'Unknown',
			notes: 'Trained on crowdsourced, open conversational data.'
		},
		{
			name: 'Jurassic-2',
			nameLink: '',
			date: '2023-03-01',
			developer: 'AI21 Labs',
			developerLink: 'https://en.wikipedia.org/wiki/AI21_Labs',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'PaLM 2',
			nameLink: 'https://en.wikipedia.org/wiki/PaLM',
			date: '2023-05-01',
			developer: 'Google',
			developerLink: 'https://en.wikipedia.org/wiki/Google',
			parameters: '340',
			corpus: '3.6 trillion tokens',
			cost: '85000',
			notes: 'Used in the Bard chatbot.'
		},
		{
			name: 'YandexGPT',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2023-05-17',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice chatbot.'
		},
		{
			name: 'Llama 2',
			nameLink: 'https://en.wikipedia.org/wiki/Llama_(language_model)',
			date: '2023-07-01',
			developer: 'Meta AI',
			developerLink: 'https://en.wikipedia.org/wiki/Meta_AI',
			parameters: '70',
			corpus: '2 trillion tokens',
			cost: '21000',
			notes: 'Trained over 3.3 million GPU (A100) hours.'
		},
		{
			name: 'Claude 2',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2023-07-01',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Claude chatbot.'
		},
		{
			name: 'Granite 13b',
			nameLink: 'https://en.wikipedia.org/wiki/IBM_Granite',
			date: '2023-07-01',
			developer: 'IBM',
			developerLink: 'https://en.wikipedia.org/wiki/IBM',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in IBM Watsonx.'
		},
		{
			name: 'Mistral 7B',
			nameLink: 'https://en.wikipedia.org/wiki/Mistral_7B',
			date: '2023-09-01',
			developer: 'Mistral AI',
			developerLink: 'https://en.wikipedia.org/wiki/Mistral_AI',
			parameters: '7.3',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'YandexGPT 2',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2023-09-07',
			developer: 'Yandex',
			developerLink: '',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice chatbot.'
		},
		{
			name: 'Claude 2.1',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_2.1',
			date: '2023-11-01',
			developer: 'Anthropic',
			developerLink: '',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Claude chatbot. Has a context window of 200,000 tokens, or ~500 pages.'
		},
		{
			name: 'Grok 1',
			nameLink: '',
			date: '2023-11-01',
			developer: 'xAI',
			developerLink: 'https://en.wikipedia.org/wiki/XAI_(company)',
			parameters: '314',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Used in the Grok chatbot. Grok 1 has a context length of 8,192 tokens and has access to X (Twitter).'
		},
		{
			name: 'DeepSeek-LLM',
			nameLink: 'https://en.wikipedia.org/wiki/DeepSeek-LLM',
			date: '2023-11-29',
			developer: 'DeepSeek',
			developerLink: 'https://en.wikipedia.org/wiki/DeepSeek',
			parameters: '67',
			corpus: '2T tokens',
			cost: '12000',
			notes: 'Trained on English and Chinese text.'
		},
		{
			name: 'Gemini 1.0',
			nameLink: 'https://en.wikipedia.org/wiki/Gemini_(language_model)',
			date: '2023-12-01',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Multimodal model, comes in three sizes. Used in the chatbot of the same name.'
		},
		{
			name: 'Mixtral 8x7B',
			nameLink: 'https://en.wikipedia.org/wiki/Mixtral_8x7B',
			date: '2023-12-01',
			developer: 'Mistral AI',
			developerLink: 'https://en.wikipedia.org/wiki/Mistral_AI',
			parameters: '46.7',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Outperforms GPT-3.5 and Llama 2 70B on many benchmarks. Mixture of experts model, with 12.9B parameters activated per token.'
		},
		{
			name: 'Phi-2',
			nameLink: 'https://en.wikipedia.org/wiki/Phi_(LLM)',
			date: '2023-12-01',
			developer: 'Microsoft',
			developerLink: 'https://en.wikipedia.org/wiki/Microsoft',
			parameters: '2.7',
			corpus: '1.4T tokens',
			cost: '419',
			notes: 'Trained on real and synthetic textbook-quality data over 14 days on 96 A100 GPUs.'
		},
		{
			name: 'Gemini 1.5',
			nameLink: 'https://en.wikipedia.org/wiki/Gemini_(language_model)',
			date: '2024-02-01',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Multimodal model based on a MoE architecture. Context window above 1 million tokens.'
		},
		{
			name: 'Gemini Ultra',
			nameLink: 'https://en.wikipedia.org/wiki/Gemini_(language_model)',
			date: '2024-02-01',
			developer: 'Google DeepMind',
			developerLink: '',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Gemma',
			nameLink: '',
			date: '2024-02-01',
			developer: 'Google DeepMind',
			developerLink: '',
			parameters: '7',
			corpus: '6T tokens',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'OLMo',
			nameLink: '',
			date: '2024-02-01',
			developer: 'Allen Institute for AI',
			developerLink: 'https://en.wikipedia.org/wiki/Allen_Institute_for_AI',
			parameters: '7',
			corpus: '2T tokens',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Claude 3',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2024-03-01',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Includes three models: Haiku, Sonnet, and Opus.'
		},
		{
			name: 'DBRX',
			nameLink: 'https://en.wikipedia.org/wiki/DBRX',
			date: '2024-03-01',
			developer: 'Databricks and Mosaic ML',
			developerLink: '',
			parameters: '136',
			corpus: '12T tokens',
			cost: 'Unknown',
			notes: 'Training cost 10 million USD.'
		},
		{
			name: 'YandexGPT 3 Pro',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2024-03-28',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in Alice chatbot.'
		},
		{
			name: 'Mixtral 8x22B',
			nameLink: '',
			date: '2024-04-17',
			developer: 'Mistral AI',
			developerLink: 'https://en.wikipedia.org/wiki/Mistral_AI',
			parameters: '141',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Phi-3',
			nameLink: 'https://en.wikipedia.org/wiki/Phi_(LLM)',
			date: '2024-04-23',
			developer: 'Microsoft',
			developerLink: 'https://en.wikipedia.org/wiki/Microsoft',
			parameters: '14',
			corpus: '4.8T tokens',
			cost: 'Unknown',
			notes: 'Marketed by Microsoft as a "small language model".'
		},
		{
			name: 'Chameleon',
			nameLink: '',
			date: '2024-05-01',
			developer: 'Meta AI',
			developerLink: 'https://en.wikipedia.org/wiki/Meta_AI',
			parameters: '34',
			corpus: '4.4 trillion',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Fugaku-LLM',
			nameLink: '',
			date: '2024-05-01',
			developer: 'Fujitsu, Tokyo Institute of Technology, etc.',
			developerLink: '',
			parameters: '13',
			corpus: '380B tokens',
			cost: 'Unknown',
			notes: 'The largest model ever trained on CPU-only, on the Fugaku supercomputer.'
		},
		{
			name: 'Granite Code',
			nameLink: 'https://en.wikipedia.org/wiki/IBM_Granite',
			date: '2024-05-01',
			developer: 'IBM',
			developerLink: 'https://en.wikipedia.org/wiki/IBM',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'YandexGPT 3 Lite',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2024-05-28',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice chatbot.'
		},
		{
			name: 'Qwen2',
			nameLink: 'https://en.wikipedia.org/wiki/Qwen2',
			date: '2024-06-01',
			developer: 'Alibaba Cloud',
			developerLink: 'https://en.wikipedia.org/wiki/Alibaba_Cloud',
			parameters: '72',
			corpus: '3T tokens',
			cost: 'Unknown',
			notes: 'Multiple sizes, the smallest being 0.5B.'
		},
		{
			name: 'DeepSeek-V2',
			nameLink: 'https://en.wikipedia.org/wiki/DeepSeek-V2',
			date: '2024-06-01',
			developer: 'DeepSeek',
			developerLink: 'https://en.wikipedia.org/wiki/DeepSeek',
			parameters: '236',
			corpus: '8.1T tokens',
			cost: '28000',
			notes: '1.4M hours on H800.'
		},
		{
			name: 'Nemotron-4',
			nameLink: '',
			date: '2024-06-01',
			developer: 'Nvidia',
			developerLink: 'https://en.wikipedia.org/wiki/Nvidia',
			parameters: '340',
			corpus: '9T tokens',
			cost: '200000',
			notes: 'Trained on 6144 H100 GPUs between December 2023 and May 2024.'
		},
		{
			name: 'Claude 3.5',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2024-06-01',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Initially only Sonnet was released. In October 2024, Sonnet 3.5 was upgraded and Haiku 3.5 became available.'
		},
		{
			name: 'Llama 3.1',
			nameLink: 'https://en.wikipedia.org/wiki/Llama_3.1',
			date: '2024-07-01',
			developer: 'Meta AI',
			developerLink: 'https://en.wikipedia.org/wiki/Meta_AI',
			parameters: '405',
			corpus: '15.6T tokens',
			cost: '440000',
			notes: '405B version took 31 million hours on H100-80GB, at 3.8E25 FLOPs.'
		},
		{
			name: 'Grok-2',
			nameLink: 'https://en.wikipedia.org/wiki/Grok-2',
			date: '2024-08-14',
			developer: 'xAI',
			developerLink: 'https://en.wikipedia.org/wiki/XAI_(company)',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Originally closed-source, then re-released as "Grok 2.5" under a source-available license in August 2025.'
		},
		{
			name: 'OpenAI o1',
			nameLink: 'https://en.wikipedia.org/wiki/OpenAI_o1',
			date: '2024-09-12',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'First LLM described as a "reasoning model".'
		},
		{
			name: 'YandexGPT 4',
			nameLink: '',
			date: '2024-10-24',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice chatbot.'
		},
		{
			name: 'Mistral Large',
			nameLink: 'https://en.wikipedia.org/wiki/Mistral_Large',
			date: '2024-11-01',
			developer: 'Mistral AI',
			developerLink: 'https://en.wikipedia.org/wiki/Mistral_AI',
			parameters: '123',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Upgraded over time. The latest version is 24.11.'
		},
		{
			name: 'Pixtral',
			nameLink: 'https://en.wikipedia.org/wiki/Pixtral',
			date: '2024-11-01',
			developer: 'Mistral AI',
			developerLink: '',
			parameters: '123',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Multimodal. There is also a 12B version which is under Apache 2 license.'
		},
		{
			name: 'OLMo 2',
			nameLink: '',
			date: '2024-11-01',
			developer: 'Allen Institute for AI',
			developerLink: 'https://en.wikipedia.org/wiki/Allen_Institute_for_AI',
			parameters: '32',
			corpus: '6.6T tokens',
			cost: '15000',
			notes: 'Initially had 7B and 13B parameter variants, with 32B released later.'
		},
		{
			name: 'Phi-4',
			nameLink: 'https://en.wikipedia.org/wiki/Phi_(LLM)',
			date: '2024-12-12',
			developer: 'Microsoft',
			developerLink: 'https://en.wikipedia.org/wiki/Microsoft',
			parameters: '14',
			corpus: '9.8T tokens',
			cost: 'Unknown',
			notes: 'Marketed by Microsoft as a "small language model".'
		},
		{
			name: 'DeepSeek-V3',
			nameLink: 'https://en.wikipedia.org/wiki/DeepSeek-V3',
			date: '2024-12-01',
			developer: 'DeepSeek',
			developerLink: 'https://en.wikipedia.org/wiki/DeepSeek',
			parameters: '671',
			corpus: '14.8T tokens',
			cost: '56000',
			notes:
				'Used 2.788M training hours on H800 GPUs. Re-released as DeepSeek-V3-0324 under MIT License in March 2025.'
		},
		{
			name: 'Amazon Nova',
			nameLink: '',
			date: '2024-12-01',
			developer: 'Amazon',
			developerLink: 'https://en.wikipedia.org/wiki/Amazon_(company)',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Includes three models: Nova Micro, Nova Lite, and Nova Pro.'
		},
		{
			name: 'DeepSeek-R1',
			nameLink: 'https://en.wikipedia.org/wiki/DeepSeek-R1',
			date: '2025-01-01',
			developer: 'DeepSeek',
			developerLink: 'https://en.wikipedia.org/wiki/DeepSeek',
			parameters: '671',
			corpus: 'Not applicable',
			cost: 'Unknown',
			notes: 'No pretraining; reinforcement-learned upon V3-Base.'
		},
		{
			name: 'Qwen2.5',
			nameLink: 'https://en.wikipedia.org/wiki/Qwen2.5',
			date: '2025-01-01',
			developer: 'Alibaba',
			developerLink: 'https://en.wikipedia.org/wiki/Alibaba_Group',
			parameters: '72',
			corpus: '18T tokens',
			cost: 'Unknown',
			notes:
				'7 dense models with parameter counts from 0.5B to 72B. Alibaba also released 2 MoE variants.'
		},
		{
			name: 'MiniMax-Text-01',
			nameLink: '',
			date: '2025-01-01',
			developer: 'Minimax',
			developerLink: 'https://en.wikipedia.org/wiki/MiniMax_(company)',
			parameters: '456',
			corpus: '4.7T tokens',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Grok 3',
			nameLink: 'https://en.wikipedia.org/wiki/Grok_3',
			date: '2025-02-01',
			developer: 'xAI',
			developerLink: 'https://en.wikipedia.org/wiki/XAI_(company)',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Training cost claimed to be "10x the compute of previous state-of-the-art models".'
		},
		{
			name: 'Gemini 2.0',
			nameLink: 'https://en.wikipedia.org/wiki/Gemini_(language_model)',
			date: '2025-02-01',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Three models released: Flash, Flash-Lite and Pro.'
		},
		{
			name: 'Claude 3.7',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2025-02-24',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'One model, Sonnet 3.7.'
		},
		{
			name: 'YandexGPT 5 Lite',
			nameLink: '',
			date: '2025-02-25',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice Neural Network chatbot.'
		},
		{
			name: 'GPT-4.5',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-4.5',
			date: '2025-02-27',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: "OpenAI's largest non-reasoning model at the time."
		},
		{
			name: 'Gemini 2.5',
			nameLink: 'https://en.wikipedia.org/wiki/Gemini_(language_model)',
			date: '2025-03-25',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Three models released: Flash, Flash-Lite and Pro.'
		},
		{
			name: 'YandexGPT 5 Lite Instruct',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2025-03-31',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice Neural Network chatbot.'
		},
		{
			name: 'Llama 4',
			nameLink: 'https://en.wikipedia.org/wiki/Llama_4',
			date: '2025-04-05',
			developer: 'Meta AI',
			developerLink: 'https://en.wikipedia.org/wiki/Meta_AI',
			parameters: '400',
			corpus: '40T tokens',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Qwen3',
			nameLink: 'https://en.wikipedia.org/wiki/Qwen3',
			date: '2025-04-01',
			developer: 'Alibaba Cloud',
			developerLink: 'https://en.wikipedia.org/wiki/Alibaba_Cloud',
			parameters: '235',
			corpus: '36T tokens',
			cost: 'Unknown',
			notes: 'Multiple sizes, the smallest being 0.6B.'
		},
		{
			name: 'OpenAI o3 / o4-mini',
			nameLink: 'https://en.wikipedia.org/wiki/OpenAI_o3',
			date: '2025-04-16',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Reasoning models.'
		},
		{
			name: 'Claude 4',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2025-05-22',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Includes two models, Sonnet and Opus.'
		},
		{
			name: 'Sarvam-M',
			nameLink: '',
			date: '2025-05-23',
			developer: 'Sarvam AI',
			developerLink: 'https://en.wikipedia.org/wiki/Sarvam_AI',
			parameters: '24',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Hybrid reasoning model fine-tuned on Mistral Small base; optimized for math, programming, and Indian languages.'
		},
		{
			name: 'Grok 4',
			nameLink: 'https://en.wikipedia.org/wiki/Grok_4',
			date: '2025-07-09',
			developer: 'xAI',
			developerLink: 'https://en.wikipedia.org/wiki/XAI_(company)',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'Param-1',
			nameLink: '',
			date: '2025-07-21',
			developer: 'BharatGen',
			developerLink: '',
			parameters: '2.9',
			corpus: "5T tokens focused on India's linguistic landscape",
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'GLM-4.5',
			nameLink: '',
			date: '2025-07-29',
			developer: 'Zhipu AI',
			developerLink: 'https://en.wikipedia.org/wiki/Zhipu_AI',
			parameters: '355',
			corpus: '22T tokens',
			cost: 'Unknown',
			notes: 'Released in 335B and 106B sizes.'
		},
		{
			name: 'GPT-OSS',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-OSS',
			date: '2025-08-05',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: '117',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Released in 20B and 120B sizes.'
		},
		{
			name: 'Claude 4.1',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2025-08-05',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Includes one model, Opus.'
		},
		{
			name: 'GPT-5',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-5',
			date: '2025-08-07',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Includes GPT-5, GPT-5 mini, and GPT-5 nano. Available in ChatGPT and API. Includes reasoning abilities.'
		},
		{
			name: 'DeepSeek-V3.1',
			nameLink: '',
			date: '2025-08-21',
			developer: 'DeepSeek',
			developerLink: 'https://en.wikipedia.org/wiki/DeepSeek',
			parameters: '671',
			corpus: '15.639T',
			cost: '',
			notes:
				'Based on DeepSeek V3; further trained on 839B tokens. A hybrid model that can switch between thinking and non-thinking modes.'
		},
		{
			name: 'YandexGPT 5.1 Pro',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2025-08-28',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Used in the Alice Neural Network chatbot.'
		},
		{
			name: 'Apertus',
			nameLink: 'https://en.wikipedia.org/wiki/Apertus_(LLM)',
			date: '2025-09-02',
			developer: 'ETH Zurich and EPF Lausanne',
			developerLink: '',
			parameters: '70',
			corpus: '15 trillion',
			cost: 'Unknown',
			notes:
				'The first LLM to be compliant with the Artificial Intelligence Act of the European Union.'
		},
		{
			name: 'Claude Sonnet 4.5',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2025-09-29',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'DeepSeek-V3.2-Exp',
			nameLink: '',
			date: '2025-09-29',
			developer: 'DeepSeek',
			developerLink: 'https://en.wikipedia.org/wiki/DeepSeek',
			parameters: '685',
			corpus: '',
			cost: '',
			notes: 'Experimental model built upon v3.1-Terminus; uses DeepSeek Sparse Attention (DSA).'
		},
		{
			name: 'GLM-4.6',
			nameLink: '',
			date: '2025-09-30',
			developer: 'Zhipu AI',
			developerLink: 'https://en.wikipedia.org/wiki/Zhipu_AI',
			parameters: '357',
			corpus: '',
			cost: '',
			notes: ''
		},
		{
			name: 'Alice AI LLM 1.0',
			nameLink: 'https://en.wikipedia.org/wiki/YandexGPT',
			date: '2025-10-28',
			developer: 'Yandex',
			developerLink: 'https://en.wikipedia.org/wiki/Yandex',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Available in the Alice AI chatbot.'
		},
		{
			name: 'Gemini 3',
			nameLink: 'https://en.wikipedia.org/wiki/Gemini_(language_model)',
			date: '2025-11-18',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Two models released: Deep Think and Pro.'
		},
		{
			name: 'Olmo 3',
			nameLink: 'https://en.wikipedia.org/wiki/List_of_large_language_models',
			date: '2025-11-20',
			developer: 'Allen Institute for AI',
			developerLink: 'https://en.wikipedia.org/wiki/Allen_Institute_for_AI',
			parameters: '32',
			corpus: '5.9T tokens',
			cost: 'Unknown',
			notes:
				'Includes 7B and 32B parameter versions, alongside reasoning and instruction-following models.'
		},
		{
			name: 'Claude Opus 4.5',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2025-11-24',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'The largest model in the Claude family.'
		},
		{
			name: 'GPT 5.2',
			nameLink: 'https://en.wikipedia.org/wiki/GPT_5.2',
			date: '2025-12-11',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Solved an open problem in statistical learning theory previously unresolved by human researchers.'
		},
		{
			name: 'GLM-4.7',
			nameLink: '',
			date: '2025-12-22',
			developer: 'Zhipu AI',
			developerLink: 'https://en.wikipedia.org/wiki/Zhipu_AI',
			parameters: '355',
			corpus: '',
			cost: '',
			notes:
				'MoE architecture. Open-source state-of-the-art on coding benchmarks. A Flash variant (30B-A3B) was released on January 19, 2026.'
		},
		{
			name: 'Qwen3-Max-Thinking',
			nameLink: '',
			date: '2026-01-26',
			developer: 'Alibaba Cloud',
			developerLink: 'https://en.wikipedia.org/wiki/Alibaba_Cloud',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'Proprietary reasoning model with adaptive tool-use, test-time scaling, and iterative self-reflection.'
		},
		{
			name: 'Kimi K2.5',
			nameLink: 'https://en.wikipedia.org/wiki/Kimi_(chatbot)',
			date: '2026-01-27',
			developer: 'Moonshot AI',
			developerLink: 'https://en.wikipedia.org/wiki/Moonshot_AI',
			parameters: '1040',
			corpus: '15T tokens',
			cost: '',
			notes:
				'Multimodal MoE with 32B active parameters. Can use Agent Swarm technology to coordinate up to 100 parallel sub-agents.'
		},
		{
			name: 'Claude Opus 4.6',
			nameLink: 'https://en.wikipedia.org/wiki/Claude_(language_model)',
			date: '2026-02-05',
			developer: 'Anthropic',
			developerLink: 'https://en.wikipedia.org/wiki/Anthropic',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'GPT-5.3-Codex',
			nameLink: 'https://en.wikipedia.org/wiki/GPT-5.3-Codex',
			date: '2026-02-05',
			developer: 'OpenAI',
			developerLink: 'https://en.wikipedia.org/wiki/OpenAI',
			parameters: 'Unknown',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: ''
		},
		{
			name: 'GLM-5',
			nameLink: '',
			date: '2026-02-12',
			developer: 'Zhipu AI',
			developerLink: 'https://en.wikipedia.org/wiki/Zhipu_AI',
			parameters: '754',
			corpus: '',
			cost: '',
			notes:
				'Specialized for agentic engineering and long-horizon tasks. Integrates DeepSeek Sparse Attention (DSA) for 200K context.'
		},
		{
			name: 'Param-2',
			nameLink: '',
			date: '2026-02-17',
			developer: 'BharatGen',
			developerLink: '',
			parameters: '17',
			corpus: '~22T tokens',
			cost: 'Unknown',
			notes: 'Mixture-of-experts model, successor of Param-1. Trained on H100 GPUs for 24 days.'
		},
		{
			name: 'Sarvam-1',
			nameLink: 'https://en.wikipedia.org/wiki/List_of_large_language_models',
			date: 'February 18, 2026[h]',
			developer: 'Sarvam AI',
			developerLink: 'https://en.wikipedia.org/wiki/Sarvam_AI',
			parameters: '105',
			corpus: '~12T tokens',
			cost: 'Unknown',
			notes:
				"India's first independently-trained foundation model; has 105B and 30B versions. Based on MoE, using only 10.3B active parameters at a time."
		},
		{
			name: 'MiMo-V2-Pro',
			nameLink: 'https://en.wikipedia.org/wiki/Xiaomi_MiMo',
			date: '2026-03-18',
			developer: 'Xiaomi',
			developerLink: 'https://en.wikipedia.org/wiki/Xiaomi',
			parameters: '1000',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes:
				'MoE model with more than 1 trillion parameters (43 billion active). Designed for agentic scenarios.'
		},
		{
			name: 'Gemma 4',
			nameLink: 'https://en.wikipedia.org/wiki/Gemma_4',
			date: '2026-04-02',
			developer: 'Google DeepMind',
			developerLink: 'https://en.wikipedia.org/wiki/Google_DeepMind',
			parameters: '31',
			corpus: 'Unknown',
			cost: 'Unknown',
			notes: 'Released in 31B, 26B A4B, E4B, and E2B variants.'
		}
	];

	// ── Geometry ────────────────────────────────────────────────────────────────
	const YEAR_W = 800; // px per year — wide enough to prevent card overlap
	const PAD_L = 48; // left padding
	const PAD_R = 64; // right padding
	const START = new Date(2018, 0, 1);
	const END_YEAR = 2027;
	const END = new Date(END_YEAR, 0, 1);
	const SPAN_MS = END.getTime() - START.getTime();
	const INNER_W = (END_YEAR - 2018) * YEAR_W + PAD_L + PAD_R;

	const AXIS_Y = 370; // y of axis line
	const CARD_W = 106; // card width
	const CARD_H = 42; // card height
	const DOT_D = 8; // dot diameter
	const CONN_PAD = 16; // gap from dot to card
	const LANE_GAP = 62; // vertical distance between lanes

	// 10 lanes: 0-4 above, 5-9 below (closest first)
	// AXIS_Y=370, CONN_PAD=16, CARD_H=42, LANE_GAP=62
	// Lane 4 (top):    370 - 16 - 42 - 62*4 = 64   ✓
	// Lane 9 (bottom): 370 + 16 + 62*4 + 42 = 676
	const LANES = [
		{ y: AXIS_Y - CONN_PAD - CARD_H, above: true }, // 0
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP, above: true }, // 1
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP * 2, above: true }, // 2
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP * 3, above: true }, // 3
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP * 4, above: true }, // 4
		{ y: AXIS_Y + CONN_PAD, above: false }, // 5
		{ y: AXIS_Y + CONN_PAD + LANE_GAP, above: false }, // 6
		{ y: AXIS_Y + CONN_PAD + LANE_GAP * 2, above: false }, // 7
		{ y: AXIS_Y + CONN_PAD + LANE_GAP * 3, above: false }, // 8
		{ y: AXIS_Y + CONN_PAD + LANE_GAP * 4, above: false } // 9
	] as const;

	const INNER_H = 676 + 42 + 36; // bottom of lane 9 card + bottom padding

	// ── Helpers ─────────────────────────────────────────────────────────────────
	function parseDate(s: string): Date {
		if (!s) return START;
		s = s.replace(/\[\w+\]/g, '').trim();
		if (/^\d{4}-\d{2}-\d{2}$/.test(s)) {
			const [y, m, d] = s.split('-').map(Number);
			return new Date(y, m - 1, d);
		}
		const md = s.match(/^(\w+)\s+(\d+),?\s*(\d{4})$/);
		if (md) return new Date(`${md[1]} ${md[2]}, ${md[3]}`);
		const my = s.match(/^(\w+)\s+(\d{4})$/);
		if (my) return new Date(`${my[1]} 1, ${my[2]}`);
		const d = new Date(s);
		return isNaN(d.getTime()) ? START : d;
	}

	function dateToX(d: Date): number {
		return PAD_L + ((d.getTime() - START.getTime()) / SPAN_MS) * ((END_YEAR - 2018) * YEAR_W);
	}

	function fmtDate(d: Date): string {
		return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
	}

	function devColor(dev: string): string {
		const d = dev.toLowerCase();
		if (d.includes('openai')) return colors.indigo;
		if (d.includes('google') || d.includes('deepmind')) return colors.cyan;
		if (d.includes('meta')) return colors.violet;
		if (d.includes('anthropic')) return colors.teal;
		if (d.includes('microsoft')) return colors.amber;
		if (d.includes('deepseek')) return colors.pink;
		if (d.includes('mistral')) return '#fb923c';
		if (d.includes('xai')) return '#e879f9';
		return colors.textSecondary;
	}

	// ── Lane assignment ──────────────────────────────────────────────────────────
	interface Positioned extends LLM {
		x: number;
		lane: number;
		color: string;
		parsedDate: Date;
	}

	const positioned: Positioned[] = (() => {
		const MIN_SEP = CARD_W + 10;
		const LANE_ORDER = [0, 5, 1, 6, 2, 7, 3, 8, 4, 9];
		const laneMax = LANES.map(() => -Infinity);

		return DATA.map((llm) => ({
			...llm,
			parsedDate: parseDate(llm.date),
			color: devColor(llm.developer),
			x: 0,
			lane: 0
		}))
			.sort((a, b) => a.parsedDate.getTime() - b.parsedDate.getTime())
			.map((ev) => {
				ev.x = dateToX(ev.parsedDate);
				let best = -1;
				for (const li of LANE_ORDER) {
					if (ev.x >= laneMax[li] + MIN_SEP) {
						best = li;
						break;
					}
				}
				if (best === -1) best = laneMax.indexOf(Math.min(...laneMax));
				laneMax[best] = ev.x;
				ev.lane = best;
				return ev;
			});
	})();

	const YEARS = Array.from({ length: END_YEAR - 2018 + 1 }, (_, i) => 2018 + i);

	// ── Pan state ────────────────────────────────────────────────────────────────
	let viewOffset = $state(0);
	let containerW = $state(1200);
	let maxOffset = $derived(Math.max(0, INNER_W - containerW));

	function pan(dir: 1 | -1) {
		const step = Math.max(containerW * 0.75, 400);
		viewOffset = Math.max(0, Math.min(maxOffset, viewOffset + dir * step));
	}

	// ── Hover state ──────────────────────────────────────────────────────────────
	let hovered = $state<Positioned | null>(null);
	let mouseX = $state(0);
	let mouseY = $state(0);
	let tipFromEvent = $state(false);
	let clearTimer: ReturnType<typeof setTimeout> | null = null;

	function enterEvent(ev: Positioned) {
		if (clearTimer) {
			clearTimeout(clearTimer);
			clearTimer = null;
		}
		hovered = ev;
		tipFromEvent = true;
	}
	function leaveEvent() {
		clearTimer = setTimeout(() => {
			if (!tipFromEvent) hovered = null;
		}, 160);
		tipFromEvent = false;
	}
	function enterTooltip() {
		if (clearTimer) {
			clearTimeout(clearTimer);
			clearTimer = null;
		}
	}
	function leaveTooltip() {
		hovered = null;
	}

	// Tooltip position
	let tipX = $derived(mouseX + 16);
	let tipY = $derived(mouseY - 8);
</script>

<svelte:window
	onmousemove={(e) => {
		mouseX = e.clientX;
		mouseY = e.clientY;
	}}
/>

<section
	style="
  background: {colors.bgPage};
  padding: {space[10]}px {space[6]}px {space[8]}px;
  min-height: 100vh;
  font-family: {typography.fontSans};
"
>
	<!-- Title -->
	<h1
		style="
    color: {colors.textPrimary};
    font-size: {typography.scale.h2}px;
    font-weight: {typography.weight.bold};
    margin: 0 0 {space[3]}px;
    text-align: center;
    letter-spacing: {typography.letterSpacing.wide}px;
  "
	>
		A Timeline of LLMs
	</h1>

	<!-- Subtitle / count -->
	<p
		style="
    color: {colors.textMuted};
    font-size: {typography.scale.body}px;
    text-align: center;
    margin: 0 0 {space[6]}px;
  "
	>
		{positioned.length} models · 2018–2026 · Hover over an event for details ·
		<a
			href="https://en.wikipedia.org/wiki/List_of_large_language_models"
			target="_blank"
			rel="noopener noreferrer">Click here for source data</a
		>
	</p>

	<!-- Color legend -->
	<div
		style="
    display: flex;
    flex-wrap: wrap;
    gap: {space[3]}px {space[5]}px;
    justify-content: center;
    margin-bottom: {space[6]}px;
  "
	>
		{#each [['OpenAI', colors.indigo], ['Google / DeepMind', colors.cyan], ['Meta', colors.violet], ['Anthropic', colors.teal], ['Microsoft', colors.amber], ['DeepSeek', colors.pink], ['Mistral', '#fb923c'], ['xAI', '#e879f9'], ['Other', colors.textSecondary]] as [label, clr]}
			<span
				style="display:flex; align-items:center; gap:{space[1]}px; font-size:{typography.scale
					.caption}px; color:{colors.textSecondary};"
			>
				<span style="width:10px; height:10px; border-radius:50%; background:{clr}; flex-shrink:0;"
				></span>
				{label}
			</span>
		{/each}
	</div>

	<!-- Arrow + viewport row -->
	<div style="display: flex; align-items: center; gap: {space[3]}px;">
		<!-- Left arrow -->
		<button
			onclick={() => pan(-1)}
			disabled={viewOffset <= 0}
			aria-label="Scroll left"
			style="
        flex-shrink: 0;
        width: 44px;
        height: 56px;
        border-radius: {radius.sm}px;
        border: 1px solid {viewOffset <= 0 ? colors.borderFaint : colors.borderDefault};
        background: {colors.bgSurface};
        color: {viewOffset <= 0 ? colors.textDim : colors.textSecondary};
        font-size: 22px;
        cursor: {viewOffset <= 0 ? 'default' : 'pointer'};
        display: flex;
        align-items: center;
        justify-content: center;
        transition: border-color 0.15s, color 0.15s;
        user-select: none;
      ">‹</button
		>

		<!-- Viewport (no scrollbar) -->
		<div
			bind:clientWidth={containerW}
			style="
        flex: 1;
        overflow: hidden;
        border: 1px solid {colors.borderDefault};
        border-radius: {radius.md}px;
        background: {colors.bgSurface};
      "
		>
			<!-- Inner canvas -->
			<div
				style="
      position: relative;
      width: {INNER_W}px;
      height: {INNER_H}px;
      background: {colors.bgSurface};
      transform: translateX(-{viewOffset}px);
      transition: transform 0.38s cubic-bezier(0.4, 0, 0.2, 1);
      will-change: transform;
    "
			>
				<!-- Year gridlines + labels -->
				{#each YEARS as yr}
					{@const xg = dateToX(new Date(yr, 0, 1))}
					<div
						style="
          position: absolute;
          left: {xg}px;
          top: 0;
          bottom: 0;
          width: 1px;
          background: {colors.borderFaint};
          pointer-events: none;
        "
					></div>
					<span
						style="
          position: absolute;
          left: {xg + 4}px;
          bottom: 10px;
          color: {colors.textDim};
          font-size: {typography.scale.caption}px;
          font-weight: {typography.weight.medium};
          user-select: none;
          pointer-events: none;
          letter-spacing: {typography.letterSpacing.wide}px;
        ">{yr}</span
					>
				{/each}

				<!-- Axis line -->
				<div
					style="
        position: absolute;
        left: 0;
        right: 0;
        top: {AXIS_Y}px;
        height: 2px;
        background: linear-gradient(to right,
          transparent 0%,
          {colors.borderDefault} 3%,
          {colors.borderDefault} 97%,
          transparent 100%);
        pointer-events: none;
      "
				></div>

				<!-- Events -->
				{#each positioned as ev}
					{@const lane = LANES[ev.lane]}
					{@const cardTop = lane.y}
					{@const isAbove = lane.above}
					{@const connTop = isAbove ? cardTop + CARD_H : AXIS_Y + DOT_D / 2}
					{@const connH = isAbove
						? AXIS_Y - DOT_D / 2 - (cardTop + CARD_H)
						: cardTop - (AXIS_Y + DOT_D / 2)}
					{@const active = hovered === ev}
					{@const cx = ev.x - CARD_W / 2}

					<!-- Connector line -->
					<div
						style="
          position: absolute;
          left: {ev.x - 0.5}px;
          top: {connTop}px;
          width: 1px;
          height: {connH}px;
          background: {ev.color};
          opacity: {active ? 0.7 : 0.25};
          transition: opacity 0.15s;
          pointer-events: none;
        "
					></div>

					<!-- Axis dot -->
					<div
						role="button"
						tabindex="0"
						aria-label={ev.name}
						style="
            position: absolute;
            left: {ev.x - DOT_D / 2}px;
            top: {AXIS_Y - DOT_D / 2}px;
            width: {DOT_D}px;
            height: {DOT_D}px;
            border-radius: {radius.full}px;
            background: {ev.color};
            box-shadow: {active ? shadow.glow(ev.color) : 'none'};
            transition: box-shadow 0.15s;
            cursor: pointer;
            z-index: 2;
          "
						onmouseenter={() => enterEvent(ev)}
						onmouseleave={leaveEvent}
						onkeydown={(e) => {
							if (e.key === 'Enter' && ev.nameLink) window.open(ev.nameLink, '_blank');
						}}
					></div>

					<!-- Card -->
					<div
						role="button"
						tabindex="-1"
						style="
            position: absolute;
            left: {cx}px;
            top: {cardTop}px;
            width: {CARD_W}px;
            height: {CARD_H}px;
            border-radius: {radius.xs}px;
            background: {active ? colors.bgSurface : `rgba(15,23,42,0.85)`};
            border: 1px solid {active ? ev.color : colors.borderSubtle};
            cursor: pointer;
            overflow: hidden;
            padding: 0 {space[2]}px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: {active ? shadow.glowSm(ev.color) : 'none'};
            transition: border-color 0.15s, box-shadow 0.15s;
            z-index: 3;
          "
						onmouseenter={() => enterEvent(ev)}
						onmouseleave={leaveEvent}
						onkeydown={(e) => {
							if (e.key === 'Enter' && ev.nameLink) window.open(ev.nameLink, '_blank');
						}}
					>
						<span
							style="
            color: {ev.color};
            font-size: {typography.scale.label}px;
            font-weight: {typography.weight.bold};
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.25;
          ">{ev.name}</span
						>
						<span
							style="
            color: {colors.textDim};
            font-size: {typography.scale.label}px;
            line-height: 1.25;
            margin-top: 2px;
          ">{fmtDate(ev.parsedDate)}</span
						>
					</div>
				{/each}
			</div>
			<!-- end inner canvas -->
		</div>
		<!-- end viewport -->

		<!-- Right arrow -->
		<button
			onclick={() => pan(1)}
			disabled={viewOffset >= maxOffset}
			aria-label="Scroll right"
			style="
        flex-shrink: 0;
        width: 44px;
        height: 56px;
        border-radius: {radius.sm}px;
        border: 1px solid {viewOffset >= maxOffset ? colors.borderFaint : colors.borderDefault};
        background: {colors.bgSurface};
        color: {viewOffset >= maxOffset ? colors.textDim : colors.textSecondary};
        font-size: 22px;
        cursor: {viewOffset >= maxOffset ? 'default' : 'pointer'};
        display: flex;
        align-items: center;
        justify-content: center;
        transition: border-color 0.15s, color 0.15s;
        user-select: none;
      ">›</button
		>
	</div>
	<!-- end arrow+viewport row -->
</section>

<!-- Tooltip (fixed, portal-like) -->
{#if hovered}
	{@const tt = hovered}
	<div
		role="tooltip"
		style="
      position: fixed;
      left: {tipX}px;
      top: {tipY}px;
      width: 300px;
      max-height: 80vh;
      overflow-y: auto;
      background: {colors.bgSurface};
      border: 1px solid {tt.color};
      border-radius: {radius.sm}px;
      padding: {space[4]}px;
      z-index: 9999;
      box-shadow: 0 8px 40px rgba(0,0,0,0.6), {shadow.glowSm(tt.color)};
      font-family: {typography.fontSans};
    "
		onmouseenter={enterTooltip}
		onmouseleave={leaveTooltip}
	>
		<!-- Model name -->
		<div
			style="margin-bottom: {space[3]}px; border-bottom: 1px solid {colors.borderSubtle}; padding-bottom: {space[3]}px;"
		>
			<span
				style="color: {tt.color}; font-size: {typography.scale.ui}px; font-weight: {typography
					.weight.bold}; line-height: {typography.lineHeight.tight};">{tt.name}</span
			>
			<div
				style="color: {colors.textMuted}; font-size: {typography.scale
					.caption}px; margin-top: {space[1]}px;"
			>
				{tt.date}
			</div>
		</div>

		<!-- Detail rows -->
		<div style="display: flex; flex-direction: column; gap: {space[2]}px;">
			<!-- Developer -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Developer
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.developer || '—'}
				</div>
			</div>

			<!-- Parameters -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Parameters (billion)
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.parameters || '—'}
				</div>
			</div>

			<!-- Corpus -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Corpus Size
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.corpus || '—'}
				</div>
			</div>

			<!-- Training cost -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Training Cost (petaFLOP-day)
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.cost || '—'}
				</div>
			</div>

			<!-- Notes -->
			{#if tt.notes}
				<div>
					<div
						style="color: {colors.textDim}; font-size: {typography.scale
							.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
							.wider}px; margin-bottom: 2px;"
					>
						Notes
					</div>
					<div
						style="color: {colors.textSecondary}; font-size: {typography.scale
							.caption}px; line-height: {typography.lineHeight.relaxed};"
					>
						{tt.notes}
					</div>
				</div>
			{/if}
		</div>
	</div>
{/if}
