
import numpy as np
import textwrap
import spacy

class WsiTokenizer:
    def split_sentence_portuguese(self, text, text_split_length=250):
        """Preprocess the input text for Portuguese language."""
        text_splits = []
        
        if text_split_length is not None and len(text) >= text_split_length:
            text_splits.append("")
            nlp = spacy.load("pt_core_news_sm")  
            nlp.add_pipe("sentencizer")
            doc = nlp(text)
            
            for sentence in doc.sents:
                if len(text_splits[-1]) + len(str(sentence)) <= text_split_length:
                    text_splits[-1] += " " + str(sentence)
                    text_splits[-1] = text_splits[-1].lstrip()
                elif len(str(sentence)) > text_split_length:
                    wrapped_lines = textwrap.wrap(
                        str(sentence),
                        width=text_split_length,
                        drop_whitespace=True,
                        break_on_hyphens=False,
                        tabsize=1,
                    )
                    text_splits.extend(wrapped_lines)  
                else:
                    text_splits.append(str(sentence))

            if len(text_splits) > 1 and text_splits[0] == "":
                del text_splits[0]
        else:
            text_splits = [text.lstrip()]

        return text_splits

