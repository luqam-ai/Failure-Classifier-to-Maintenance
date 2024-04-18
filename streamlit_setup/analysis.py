import streamlit as st

def main():
    st.title('Zbiór danych awaryjności maszyn')
    st.subheader("Próbka danych")
    st.markdown("Zestaw danych zawiera 10 000 punktów danych, z których każdy ma 14 cech. \
            Te cechy obejmują unikalne identyfikatory (UID) produktów oznaczone literami L, M lub H, \
            reprezentujące warianty: \
            niskiej, średniej i wysokiej jakości,\
            temperaturę powietrza, temperaturę procesu, \
            prędkość obrotową, moment obrotowy, zużycie narzędzia oraz etykietę awaria maszyny, wskazującą, czy doszło do awarii podczas procesu.")
    
    st.markdown("Etykieta awaria maszyny jest określana przez pięć niezależnych trybów awarii: awarię zużycia narzędzia (TWF), \
            awarię odprowadzania ciepła (HDF), awarię zasilania (PWF), awarię przeciążenia (OSF) oraz losowe awarie (RNF). \
            Każdy tryb awarii ma określone warunki prowadzące do awarii procesu, takie jak osiągnięcie przez zużycie narzędzia określonego progu, \
            powodowanie różnic temperatur przez odprowadzanie ciepła, przekraczanie wymagań zasilania lub losowe zdarzenia awaryjne. \
            Zestaw danych prezentuje scenariusz, w którym etykieta awaria maszyny wskazuje, czy którykolwiek z zdefiniowanych \
            trybów awarii wystąpił podczas procesu. Informacja ta jest kluczowa dla strategii konserwacji zapobiegawczej oraz zrozumienia \
            wydajności sprzętu w różnych warunkach.")
    
    st.subheader("kategorie awarii")
    st.image('images/types_distribution.png')
    
    st.subheader("Rozkłady badanych cech")
    st.image('images/features_hist.png')
    st.image('images/features_boxplot.png')
    st.markdown("Kolumny Temperatura_powietrza, Temperatura_procesu i moment obrotowy są podobne do rozkładu normalnego,\
                a prędkość obrotowa jest asymetryczna z ujemnym obciążeniem. Wykres pudełkowy, pozwala potwierdzić hipotezę,\
                że istnieją wartości odstające w niektórych kolumnach. Jednakże, nie usuwamy tych wartości, \
                ponieważ ma sens, że gdy maszyna ulegnie awarii, pomiary dokonywane przez niektóre sensory wzrosną znacznie. Ponadto, \
                gdy prędkość obrotowa wzrasta, moment obrotowy również spada - jest to zachowanie fizyczne, \
                więc wykryte wartości odstające w kolumnie momentu obrotowego o niskich wartościach mogą być tym właśnie spowodowane.")
    
    
    st.subheader("Analiza korelacji między cechami")
    st.image('images/corr.png')
    st.markdown("Hipoteza, że gdy wzrasta moment obrotowy, maleje prędkość obrotowa, jest prawdziwa! \
                Istnieje wyraźna ujemna korelacja między tymi cechami (-0.88). Ponadto, możemy teraz zobaczyć, \
                że temperatura procesu i temperatura powietrza mają również wyraźną korelację. Gdy temperatura powietrza rośnie, \
                temperatura procesu również rośnie, a to dzieje się w przeciwnym kierunku.")
    
    st.subheader("Analiza PCA")
    st.markdown("Analiza składowych głównych (PCA - Principal Component Analysis) redukuje wielkość danych, \
                uwydatnia wzorce i upraszcza zbiory danych, poprawiając wydajność i interpretowalność modelu, \
                jednocześnie zachowując istotne informacje. Sprawdźmy, ile komponentów wyjaśnia więcej lub mniej \
                niż 95% naszych danych na podstawie poniższego wykresu.")
    st.image('images/pca.png')
    st.markdown("Możemy zauważyć, że przy użyciu 4 składowych już wyjaśniliśmy zmienność naszych danych na poziomie około 94%.\
                Dlatego możemy spróbować użyć tylko tych składowych do modelowania i analizowania, czy to poprawi wydajność. \
                W niektórych przypadkach zbiór danych może być krytyczny, a utrata 6% informacji może pogorszyć model.\
                Zobaczmy, co wyjaśnia każda składowa:")
    st.image('images/pca_components.png')
    st.markdown("Jak można zauważyć: \
        PC1 i PC2: wyjaśnione przez Temperaturę_powietrza, Temperaturę_procesu, Prędkość_obrotową i Moment_obrotowy;\
        PC3: wyjaśnione przez Zużycie_narzędzia;\
        PC4: najbardziej wyjaśnione przez Typ_Niski i Typ_Średni;\
        PC5: najbardziej wyjaśnione przez Typ_Wysoki;\
        PC6: najbardziej wyjaśnione przez Temperaturę_powietrza, Temperaturę_procesu, Prędkość_obrotową i Moment_obrotowy;\
        PC7: najbardziej wyjaśnione przez Temperaturę_powietrza, Temperaturę_procesu, Prędkość_obrotową i Moment_obrotowy."
    )
    
    st.subheader("Modelowanie danych")
    st.markdown("Modelowanie z użyciem technik Machine Learning w kontekście prognozowania awarii maszyn ma na celu przewidywania momentów, \
                w których maszyny mogą ulec awarii lub wymagać konserwacji. Poprzez analizę danych telemetrycznych, takich jak temperatury, \
                prędkości obrotowe, zużycie narzędzi itp., model jest w stanie wykrywać wzorce lub anomalie, które mogą wskazywać na potencjalne \
                problemy lub awarie w przyszłości. Modelowanie to umożliwia firmom przemysłowym wdrożenie strategii konserwacji zapobiegawczej, \
                co może znacząco zwiększyć dostępność maszyn, zmniejszyć koszty napraw i poprawić wydajność produkcji.")
    

if __name__ == "__main__":
    main()