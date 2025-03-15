import pandas as pd
import logging
import argparse
from colorama import init, Fore, Style

init(autoreset=True)
logging.basicConfig(level=logging.INFO, format='%(message)s')

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df['CSV_Line'] = df.index + 2
        if 'Result' in df.columns:
            df['Result'] = df['Result'].str.upper().str.strip()
            logging.info(f"{Fore.CYAN}Valores únicos em 'Result': {df['Result'].unique()}{Style.RESET_ALL}")
        else:
            logging.warning(f"{Fore.YELLOW}Coluna 'Result' não encontrada.{Style.RESET_ALL}")
        return df
    except Exception as e:
        logging.error(f"{Fore.RED}Erro ao carregar CSV: {e}{Style.RESET_ALL}")
        return None

def identify_errors(df, error_list):
    if df is not None and 'Result' in df.columns:
        error_list = [e.upper().strip() for e in error_list]
        logging.info(f"{Fore.CYAN}Procurando por: {error_list}{Style.RESET_ALL}")
        error_df = df[df['Result'].isin(error_list)]
        return error_df
    return pd.DataFrame()

def generate_feedback(error_df, feedback_dict):
    feedback = []
    for _, row in error_df.iterrows():
        error = row['Result']
        line = row['CSV_Line']
        fb = feedback_dict.get(error, "Erro desconhecido.")
        feedback.append(
            f"{Fore.RED}Linha {line:<4}{Style.RESET_ALL} | "
            f"{Fore.YELLOW}{error:<20}{Style.RESET_ALL} | "
            f"{Fore.CYAN}{fb}{Style.RESET_ALL}"
        )
    return feedback

def main(file_path, error_list, feedback_dict):
    logging.info(f"{Fore.MAGENTA}{Style.BRIGHT}===== Análise Iniciada ====={Style.RESET_ALL}")
    df = load_csv(file_path)
    if df is None:
        return
    error_df = identify_errors(df, error_list)
    if not error_df.empty:
        logging.info(f"{Fore.MAGENTA}{Style.BRIGHT}===== Erros Encontrados ====={Style.RESET_ALL}")
        logging.info(f"{Fore.WHITE}Linha | Tipo de Erro          | Feedback{Style.RESET_ALL}")
        logging.info(f"{Fore.WHITE}{'-' * 60}{Style.RESET_ALL}")
        for fb in generate_feedback(error_df, feedback_dict):
            logging.info(fb)
    else:
        logging.info(f"{Fore.GREEN}Nenhum erro encontrado.{Style.RESET_ALL}")
    logging.info(f"{Fore.MAGENTA}{Style.BRIGHT}===== Resumo ====={Style.RESET_ALL}")
    logging.info(f"{Fore.GREEN}Total de erros: {len(error_df)}{Style.RESET_ALL}")
    logging.info(f"{Fore.MAGENTA}{Style.BRIGHT}===== Análise Concluída ====={Style.RESET_ALL}")

ERROR_LIST = ['ACCESS DENIED', 'FILE NOT FOUND', 'BUFFER OVERFLOW']
FEEDBACK_DICT = {
    'ACCESS DENIED': "Verifique permissões.",
    'FILE NOT FOUND': "Confirme o caminho.",
    'BUFFER OVERFLOW': "Possível problema de software."
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analisador de logs.")
    parser.add_argument("file_path", help="Caminho do CSV.")
    args = parser.parse_args()
    main(args.file_path, ERROR_LIST, FEEDBACK_DICT)