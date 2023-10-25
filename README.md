# Llama Store demos

This repo contains a set of Python demos using the [liblab llama store](https://github.com/liblaber/llama-store). These demos compare the API to an SDK.

This project includes a dev container, and this is the recommended way to run. You can read more in the [VS Code dev containers docs](https://code.visualstudio.com/docs/devcontainers/containers).

## Run the llama store

The llama store is included as a Git submodule, so it will need to be initialized:

```bash
git submodule update --init --recursive
```

> If you are using the included dev container, the submodule will be included for you.

You will also need to set up the llama store project by installing the relevant Python packages, as well as seeding the database. There is a helper script to do this.

```bash
python -m venv .venv            # Create a virtual env
source ./.venv/bin/activate     # Activate the virtual env
./scripts/setup-llama-store.sh  # Setup the llama store project
```

> If you are using the included dev container, this will already be run for you.

You can then run the llama store using the helper script:

```bash
./scripts/run-llama-store.sh
```

You can reset the llama store by re-running the setup script. This will delete any newly created users, restore the llamas and return the database to its initial state. You will need to stop the API before running this script, then restart it afterwards.

```bash
./scripts/setup-llama-store.sh
```

## Generate an SDK for the llama store

An SDK for the llama store can be generated using the [liblab CLI](https://developers.liblab.com/cli/cli-overview). This can be installed using `npm`:

```bash
npm install -g liblab
```

> If you are using the included dev container, this will already be installed for you.

First you need to log in to the liblab CLI:

```bash
liblab login
```

If you don't have an account, you can register with this command.

You can then generate an SDK using the spec files in the `llama-store` submodule:

```bash
cd llama-store
liblab build
```

## Demos

All the demos are in the [`demos`](./demos/) folder.

| Demo                              | Description |
| --------------------------------- | ----------- |
| [API vs SDK](./demos/api-vs-sdk/) | A set of demos comparing the developer experience of accessing the llama store using its API, vs using the generated SDK from liblab. |

