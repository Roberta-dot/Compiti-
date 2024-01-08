-- Creazione di una tabella che possa contenere i dati del CSV:
CREATE TABLE vendite (
    ID_transazione INT,
    Categoria VARCHAR(255),
    Costo DECIMAL(10, 2),
    Sconto DECIMAL(10, 2)
);

INSERT INTO vendite (ID_transazione, Categoria, Costo, Sconto) VALUES
(1, 'Informatica', 500, 20),
(2, 'Cucina', 120, 0),
(3, 'Abbigliamento', 235,30),
(4, 'Libri', 25, 0),
(5, 'Informatica', 890, 55),
(6, 'Informatica', 125.80, 5),
(7, 'Cucina', 34, 20),
(8, 'Abbigliamento', 62.20,2.50),
(9, 'Libri', 27, 1.50),
(10, 'Informatica', 15, 0),
(11, 'Abbigliamento', 43.25, 3.50),
(12, 'Cucina', 120, 0),
(13, 'Abbigliamento', 235,30),
(14, 'Libri', 25, 0),
(15, 'Cucina', 1500, 800),
(16, 'Informatica', 946.60, 11),
(17, 'Cucina', 13.25, 1.34),
(18, 'Abbigliamento', 423.89, 5),
(19, 'Libri', 36.70, 0),
(20, 'Abbigliamento', 68.45, 3.40),
(21, 'Informatica', 328.65, 0),
(22, 'Cucina', 600, 16),
(23, 'Abbigliamento', 17.89,0),
(24, 'Libri', 53.10, 2.60),
(25, 'Informatica', 1750, 32),
(26, 'Informatica', 24, 0),  
(27, 'Cucina', 46, 1.24),
(28, 'Informatica', 1300, 24.90),
(29, 'Abbigliamento', 65, 6.50),
(30, 'Abbigliamento', 264, 23.80);

    
CREATE TABLE dettagli_vendite (
    ID_transazione INTEGER,
    Data_transazione DATE,
    Quantità INTEGER
);

INSERT INTO dettagli_vendite (ID_transazione, Data_transazione, Quantità) VALUES
(1, '2023.03.05', 14),
(2, '2023.12.21', 35),
(3, '2023.11.26', 19),
(4, '2023.02.04', 10),
(5, '2023.05.08', 9),
(6, '2023.04.13', 20),
(7, '2023.01.22', 28),
(8, '2023.06.07', 4),
(9, '2023.02.22', 2),
(10, '2023.07.27', 34),
(11, '2023.07.08', 17),
(12, '2023.04.30', 37),
(13, '2023.08.11', 1),
(14, '2023.09.19', 54),
(15, '2023.09.23', 1),
(16, '2023.07.20', 2),
(17, '2023.10.05', 50),
(18, '2023.11.09', 3),
(19, '2023.09.20', 55),
(20, '2023.06.15', 34),
(21, '2023.12.21', 39),
(22, '2023.05.04', 8),
(23, '2023.01.10', 44),
(24, '2023.12.09', 1),
(25, '2023.06.17', 3),
(26, '2023.10.30', 35),
(27, '2023.02.06', 53),
(28, '2023.03.18', 23),
(29, '2023.01.23', 11),
(30, '2023.03.06', 2);   

SELECT * FROM vendite;

SELECT * FROM dettagli_vendite;

#Punto3 esercizio
SELECT * FROM dettagli_vendite WHERE Data_transazione = '06.02.2023';

SELECT * FROM vendite WHERE Sconto/Costo>0.5;



#punto4 esercizio
SELECT Categoria, SUM(Costo) AS Totale_vendite
FROM vendite
GROUP BY Categoria
HAVING Totale_vendite > 0; 



SELECT v.Categoria, SUM(dv.Quantità) AS Totale_prodotti_venduti
FROM vendite v
JOIN dettagli_vendite dv ON v.ID_transazione = dv.ID_transazione
GROUP BY v.Categoria;


#punto5 esercizio
SELECT Data_transazione 
FROM dettagli_vendite 
WHERE Data_transazione >'2023-10-01';

#punto5 esercizio
SELECT * 
FROM dettagli_vendite 
WHERE Data_transazione >'2023-10-01';


SELECT 
    YEAR(dv.Data_transazione) AS Anno,
    MONTH(dv.Data_transazione) AS Mese,
    SUM(v.Costo) AS Totale_vendite
FROM vendite v
JOIN dettagli_vendite dv ON v.ID_transazione = dv.ID_transazione
WHERE dv.Data_transazione >= CURDATE() - INTERVAL 12 MONTH
GROUP BY Anno, Mese
ORDER BY Anno, Mese;

#punto7 esercizio
SELECT Categoria, AVG(Sconto) AS ScontoMedio
FROM vendite
GROUP BY Categoria
ORDER BY ScontoMedio DESC
LIMIT 1;

#punto8 esercizio
#Il punto5 contiene i dati necessari per la nostra analisi: i mesi più redditizi per il negozio risultano essere marzo, giugno e settembre, mentre i mesi che riscontrano le vendite minori sono ottobre, gennaio e febbraio.  
SELECT 
    YEAR(dv.Data_transazione) AS Anno,
    MONTH(dv.Data_transazione) AS Mese,
    SUM(v.Costo) AS Totale_mese,
    LAG(SUM(v.Costo)) OVER (ORDER BY YEAR(dv.Data_transazione), MONTH(dv.Data_transazione)) AS Totale_mese_precedente,
    CASE 
        WHEN LAG(SUM(v.Costo)) OVER (ORDER BY YEAR(dv.Data_transazione), MONTH(dv.Data_transazione)) IS NOT NULL
            THEN SUM(v.Costo) - LAG(SUM(v.Costo)) OVER (ORDER BY YEAR(dv.Data_transazione), MONTH(dv.Data_transazione))
        ELSE 0
    END AS Incremento_decremento
FROM vendite v
JOIN dettagli_vendite dv ON v.ID_transazione = dv.ID_transazione
GROUP BY Anno, Mese
ORDER BY Anno, Mese;



#punto9 esercizio: dividiamo le stagioni in due
#i primi 6 mesi dell'anno abbiamo 5895.34, 3999.47 nei restanti mesi, per cui possiamo dire che la prima stagione è più redditizia. 